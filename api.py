from fastapi import FastAPI
from pydantic import BaseModel
from retrieve import summary  # Import your summary function

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

# POST endpoint
@app.post("/query")
async def query_retrieval(request: QueryRequest):
    query_text = request.query
    results = summary(query_text)  # Call the summarization logic from retrieve.py
    return {"query": query_text, "results": results}

# GET endpoint
@app.get("/search")
async def query_retrieval(query: str):
    results = summary(query)  # Call the summarization logic from retrieve.py
    return {"query": query, "results": results}
