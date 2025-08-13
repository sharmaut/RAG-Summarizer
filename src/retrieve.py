import json
import torch
from transformers import pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Load stored embeddings from ChromaDB
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)

# Load chunked data
with open("chunked_data.json", "r") as f:
    chunked_data = json.load(f)

# Load summarization model
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0 if device != "cpu" else -1)

# Function to handle retrieval, filtering, and summarization
def summary(query_text: str, k=5, similarity_threshold=0.9):
    """
    Retrieves relevant documents based on semantic similarity.
    Filters out low-relevance results using a similarity threshold.
    Generates concise summaries.
    """

    # Retrieve documents with similarity scores
    retrieved_docs_with_scores = vectorstore.similarity_search_with_score(query_text, k=k)

    result_list = []
    seen_ids = set()  # Avoid duplicate documents

    for doc, score in retrieved_docs_with_scores:
        if score < similarity_threshold:  # Skip low-relevance results
            continue

        chunk_text = doc.page_content
        doc_id = doc.metadata.get("doc_id", "Unknown")  # Ensure metadata retrieval

        # Generate summary dynamically based on chunk length
        input_length = len(chunk_text.split())
        max_summary_length = max(50, min(200, input_length // 2))  # More flexible length

        summary_text = summarizer(chunk_text, max_length=max_summary_length, min_length=30, do_sample=False)[0]["summary_text"]

        # Ensure no duplicate entries
        if doc_id not in seen_ids:
            result_list.append({
                "id": doc_id,
                "chunk": chunk_text,
                "summary": summary_text
            })
            seen_ids.add(doc_id)

    return result_list
