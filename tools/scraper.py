import random
import time
from bs4 import BeautifulSoup
import requests

class WebScraper:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        ]
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }
    
    def scrape(self, url, max_retries=2):
        for attempt in range(max_retries):
            try:
                self.headers["User-Agent"] = random.choice(self.user_agents)
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                
                if len(response.text) < 500:
                    raise ValueError("Page content too small")
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for element in soup(['script', 'style', 'nav', 'footer', 'iframe', 'aside', 'form']):
                    element.decompose()
                
                text = ' '.join(soup.stripped_strings)
                if not text or len(text) < 100:
                    raise ValueError("Insufficient text content")
                
                return text
                
            except Exception as e:
                print(f"Attempt {attempt + 1} failed for {url}: {str(e)}")
                if attempt == max_retries - 1:
                    return None
                time.sleep(2 ** attempt)