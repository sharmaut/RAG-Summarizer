import requests
from bs4 import BeautifulSoup
import csv
import json

# WHO Publications URL
URL = "https://www.who.int/publications/who-guidelines"

# Headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_guidelines(url):
    """Fetch WHO guidelines page content."""
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print("✅ Status Code: 200 - Page content retrieved successfully.")
        return response.text
    else:
        print(f"❌ Failed to retrieve page, status code: {response.status_code}")
        return None

def parse_guidelines(html):
    """Extract guideline titles, dates, and links."""
    soup = BeautifulSoup(html, "html.parser")
    guidelines_data = []

    guidelines = soup.find_all("div", class_="sf-publications-item")

    for guideline in guidelines:
        title_tag = guideline.find("h3", class_="sf-publications-item__title")
        date_tag = guideline.find("div", class_="sf-publications-item__date")
        link_tag = guideline.find("a", href=True)

        title = title_tag.text.strip() if title_tag else "No title"
        date = date_tag.text.strip() if date_tag else "No date"
        link = link_tag["href"] if link_tag else "No link"

        # Ensure the link is absolute
        if link.startswith("/"):
            link = "https://www.who.int" + link

        guidelines_data.append({"title": title, "date": date, "link": link})

    return guidelines_data

def save_to_csv(data, filename="guidelines.csv"):
    """Save extracted guidelines to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "date", "link"])
        writer.writeheader()
        writer.writerows(data)
    print(f"📂 Data saved to {filename}")

if __name__ == "__main__":
    html_content = fetch_guidelines(URL)
    if html_content:
        guidelines = parse_guidelines(html_content)

        if guidelines:
            print(f"✅ Found {len(guidelines)} guidelines.")
            save_to_csv(guidelines)
        else:
            print("⚠️ No guidelines found.")
