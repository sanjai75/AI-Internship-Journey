from sentence_transformers import SentenceTransformer


def create_chunks(documents, chunk_size=500):

    chunks = []

    for doc in documents:

        text = doc["text"]

        for i in range(0, len(text), chunk_size):

            chunks.append({
                "text": text[i:i + chunk_size],
                "file": doc["file"],
                "page": doc["page"]
            })

    return chunks


def generate_embeddings(chunks):

    print("Loading Embedding Model...")

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    print("Embedding Model Ready")

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = model.encode(
        texts
    ).tolist()

    print(
        f"Generated {len(embeddings)} embeddings."
    )

    return model, embeddings