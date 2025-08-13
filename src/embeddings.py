import chromadb
from sentence_transformers import SentenceTransformer
import json

# Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="medical_guidelines")

# Load the chunked data
with open("chunked_data.json", "r") as f:
    data = json.load(f)

# Store document chunks along with embeddings
for doc in data:
    doc_id = doc["doc_id"]
    chunk_id = f"{doc_id}_chunk_{doc['chunk_num']}"
    text = doc["chunk_text"]

    embedding = embedding_model.encode(text).tolist()

    collection.add(
        ids=[chunk_id],
        embeddings=[embedding],
        documents=[text]  # 🔹 Ensure text is stored
    )

print("Embeddings stored successfully in ChromaDB!")
