import json
import textwrap
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load WHO Guidelines CSV
df = pd.read_csv("guidelines.csv")

chunk_size = 500 

chunked_data = []

# Function to scrape text from WHO guideline pages
def scrape_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract all text content
        paragraphs = soup.find_all("p")  
        content = " ".join([p.get_text() for p in paragraphs])

        return content.strip()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""

# Process each document
for i, row in df.iterrows():
    doc_id = f"doc_{i}"
    url = row["link"]
    text = scrape_text(url)  # Fetch full text from the URL

    if not text:
        print(f"Skipping {url} due to missing content.")
        continue

    # Split into chunks
    chunks = textwrap.wrap(text, chunk_size)

    for chunk_num, chunk in enumerate(chunks):
        chunked_data.append({
            "doc_id": doc_id,
            "chunk_num": chunk_num,
            "chunk_text": chunk
        })

with open("chunked_data.json", "w") as f:
    json.dump(chunked_data, f, indent=4)

print("Chunking complete! Data saved in chunked_data.json")
