from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read documents
with open("documents.txt", "r") as f:
    documents = [line.strip() for line in f if line.strip()]

# Generate embeddings
embeddings = model.encode(documents, convert_to_numpy=True)

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, "faiss_index.index")
with open("doc_store.txt", "w") as f:
    for doc in documents:
        f.write(doc + "\n")

print("✅ Embeddings generated and index saved.")
