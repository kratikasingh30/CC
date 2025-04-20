from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline

# Load model and index
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("faiss_index.index")

# Load stored documents
with open("doc_store.txt", "r") as f:
    documents = [line.strip() for line in f]

# Input user query
query = input("🔍 Ask a question: ")
query_embedding = model.encode([query])

# Search
top_k = 2
D, I = index.search(query_embedding, top_k)

# Retrieve context
retrieved = [documents[idx] for idx in I[0]]
context = " ".join(retrieved)

# Generate answer
generator = pipeline("text-generation", model="gpt2")
prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
response = generator(prompt, max_length=100, do_sample=True)[0]['generated_text']

print("\n📚 Retrieved Context:")
for doc in retrieved:
    print("-", doc)

print("\n🧠 Generated Answer:")
print(response)
