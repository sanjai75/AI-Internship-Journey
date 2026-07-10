import os
import glob
from dotenv import load_dotenv
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
from openai import OpenAI

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise Exception("OPENROUTER_API_KEY not found in .env")

# -----------------------------
# OpenRouter Client
# -----------------------------
client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://localhost",
        "X-Title": "RAG Document Assistant"
    }
)
# -----------------------------
# Load Multiple PDFs
# -----------------------------
text = ""

pdf_files = glob.glob("data/*.pdf")

print(f"Found {len(pdf_files)} PDF files.\n")

for pdf in pdf_files:
    print(f"Loading: {pdf}")

    reader = PdfReader(pdf)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

print("\nAll PDF files loaded successfully!")
print("Total Characters:", len(text))

# -----------------------------
# Split Text into Chunks
# -----------------------------
chunk_size = 500

chunks = []

for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i+chunk_size])

print("Chunks Created:", len(chunks))

# -----------------------------
# Load Embedding Model
# -----------------------------
print("Loading Embedding Model...")

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Embedding Model Ready")
# -----------------------------
# Generate Embeddings
# -----------------------------
print("Generating Embeddings...")

embeddings = embedding_model.encode(chunks).tolist()

print(f"Generated {len(embeddings)} embeddings.")

# -----------------------------
# Create ChromaDB
# -----------------------------
print("Creating ChromaDB...")

chroma_client = chromadb.PersistentClient(path="./vector_db")

collection = chroma_client.get_or_create_collection(
    name="rag_collection"
)

# Clear old data (optional)
try:
    collection.delete(ids=collection.get()["ids"])
except:
    pass

# Store chunks + embeddings
ids = [f"chunk_{i}" for i in range(len(chunks))]

collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings
)

print("Embeddings stored successfully in ChromaDB!")
# -----------------------------
# Ask User Question
# -----------------------------
while True:
    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Convert question into embedding
    query_embedding = embedding_model.encode(question).tolist()

    # Search similar chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    retrieved_docs = "\n".join(results["documents"][0])

    print("Retrieved Chunks:")

    for i, doc in enumerate(results["documents"][0], start=1):
        print(f"\nChunk {i}:")
        print(doc[:200] + "...")

    print("\nRelevant Context Found!\n")

    response = client.chat.completions.create(
        model="tencent/hy3:free",
        messages=[
            {
                "role": "system",
                "content": "Answer ONLY from the given context. If the answer is not found, say 'Not found in the document.'"
            },
            {
                "role": "user",
                "content": f"""
Context:
{retrieved_docs}

Question:
{question}
"""
            }
        ]
    )

    print("\n==============================")
    print("Answer:\n")
    print(response.choices[0].message.content)
    print("==============================")
    print(f"\nChunk {i}:")
    print(doc[:200] + "...")

    print("\nRelevant Context Found!\n")

    response = client.chat.completions.create(
        model="tencent/hy3:free",
        messages=[
            {
                "role": "system",
                "content": "Answer ONLY from the given context. If the answer is not found, say 'Not found in the document.'"
            },
            {
                "role": "user",
                "content": f"""
Context:
{retrieved_docs}

Question:
{question}
"""
            }
        ]
    )

    print("\n==============================")
    print("Answer:\n")
    print(response.choices[0].message.content)
    print("==============================")

