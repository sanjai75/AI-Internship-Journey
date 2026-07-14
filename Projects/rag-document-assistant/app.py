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
documents = []

pdf_files = glob.glob("data/*.pdf")
if len(pdf_files) == 0:
    print("❌ No PDF files found in the data folder.")
    exit()

print(f"Found {len(pdf_files)} PDF files.\n")

for pdf in pdf_files:
    print(f"Loading: {pdf}")

    reader = PdfReader(pdf)

    for page_no, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()

        if page_text:
            documents.append({
                "file": os.path.basename(pdf),
                "page": page_no,
                "text": page_text
            })

print("\nAll PDF files loaded successfully!")

total_chars = sum(len(doc["text"]) for doc in documents)
print("Total Characters:", total_chars)
# -----------------------------
# Split Text into Chunks
# -----------------------------
chunk_size = 500

chunks = []

for doc in documents:
    text = doc["text"]

    for i in range(0, len(text), chunk_size):
        chunks.append({
            "text": text[i:i+chunk_size],
            "file": doc["file"],
            "page": doc["page"]
        })
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

texts = [c["text"] for c in chunks]

embeddings = embedding_model.encode(texts).tolist()

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
    documents=[c["text"] for c in chunks],
    embeddings=embeddings,
    metadatas=[
        {
            "file": c["file"],
            "page": c["page"]
        }
        for c in chunks
    ]
)

print("Embeddings stored successfully in ChromaDB!")
print("\n===================================")
print("📄 Welcome to RAG Document Assistant")
print("Ask questions from your PDF documents.")
print("Type 'exit' anytime to quit.")
print("===================================\n")
# -----------------------------
# Ask User Question
# -----------------------------
while True:
    question = input("\nAsk a question (type 'exit' to quit): ")
    if question.strip() == "":
      print("⚠ Please enter a valid question.")
      continue

    if question.lower() == "exit":
      print("\n👋 Thank you for using RAG Document Assistant!")
      print("Goodbye!\n")
      break
    # Convert question into embedding
    query_embedding = embedding_model.encode(question).tolist()
    print("\n⏳ Processing your question...")

    # Search similar chunks
    results = collection.query(
            query_embeddings=[query_embedding],
            n_results=2
        )
    metadata = results["metadatas"][0][0]

    print("\nSource Information")
    print("------------------------")
    print("Document :", metadata["file"])
    print("Page     :", metadata["page"])
    print("Snippet  :", results["documents"][0][0][:150], "...")

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
        