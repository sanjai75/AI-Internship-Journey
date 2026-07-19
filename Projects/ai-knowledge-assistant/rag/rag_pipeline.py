import chromadb


class RAGPipeline:

    def __init__(self, chunks, embeddings):

        self.chunks = chunks

        print("Creating ChromaDB...")

        self.chroma_client = chromadb.PersistentClient(
            path="./vector_db"
        )

        self.collection = self.chroma_client.get_or_create_collection(
            name="rag_collection"
        )

        # Clear old data
        try:
            old_ids = self.collection.get()["ids"]

            if old_ids:
                self.collection.delete(
                    ids=old_ids
                )

        except Exception:
            pass

        # Create IDs
        ids = [
            f"chunk_{i}"
            for i in range(len(chunks))
        ]

        # Store chunks and embeddings
        self.collection.add(
            ids=ids,
            documents=[
                chunk["text"]
                for chunk in chunks
            ],
            embeddings=embeddings,
            metadatas=[
                {
                    "file": chunk["file"],
                    "page": chunk["page"]
                }
                for chunk in chunks
            ]
        )

        print("Embeddings stored successfully!")

    def search(
        self,
        query_embedding,
        n_results=2
    ):

        results = self.collection.query(
            query_embeddings=[
                query_embedding
            ],
            n_results=n_results
        )

        return results