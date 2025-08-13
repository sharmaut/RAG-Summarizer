from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd

def scrape_pubmed(query, max_results=10):
    """
    Scrapes PubMed for published articles related to a medical query.
    
    :param query: Search term (e.g., "Diabetes treatment").
    :param max_results: Number of articles to retrieve.
    :return: List of dictionaries containing title, URL, and abstract.
    """
    articles = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        search_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={query.replace(' ', '+')}"
        page.goto(search_url)
        
        soup = BeautifulSoup(page.content(), "html.parser")
        results = soup.select(".docsum-content")[:max_results]

        for result in results:
            title_elem = result.select_one(".docsum-title")
            if title_elem:
                title = title_elem.get_text(strip=True)
                link = "https://pubmed.ncbi.nlm.nih.gov" + title_elem["href"]
                
                # Open article page to extract abstract
                page.goto(link)
                article_soup = BeautifulSoup(page.content(), "html.parser")
                abstract_elem = article_soup.select_one(".abstract-content")
                abstract = abstract_elem.get_text(strip=True) if abstract_elem else "No abstract available"
                
                articles.append({"title": title, "url": link, "abstract": abstract})
        
        browser.close()
    
    return articles

# Example Usage
query = "Diabetes treatment"
articles = scrape_pubmed(query)

# Save results to CSV
df = pd.DataFrame(articles)
df.to_csv("pubmed_articles.csv", index=False)

print(df)
