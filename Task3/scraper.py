
import requests
from bs4 import BeautifulSoup

def fetch_headlines(url="https://www.flipkart.com/"):
    page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(page.text, "html.parser")
    
    headlines = [h.get_text(strip=True) for h in soup.find_all("h2")]
    
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for h in headlines:
            f.write(h + "\n")
    return headlines

if __name__ == "__main__":
    print("--- Fetching Headlines ---")
    headlines = fetch_headlines()
    if headlines:
        print(f"✅ {len(headlines)} headlines saved to headlines.txt")
    else:
        print("❌ No headlines found.")
