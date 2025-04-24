import random
import time
from bs4 import BeautifulSoup
import requests

class WebScraper: #agents to simulate different web browsers 
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        ]
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", #headers for making web requests 
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }
    # Method to scrape the content from the given URL with retry mechanism
    def scrape(self, url, max_retries=2):
        for attempt in range(max_retries): # Loop through retry attempts
            try:
                self.headers["User-Agent"] = random.choice(self.user_agents)
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                
                if len(response.text) < 500: # Check if the content is too small
                    raise ValueError("Page content too small")
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for element in soup(['script', 'style', 'nav', 'footer', 'iframe', 'aside', 'form']): #Remove unwanted HTML elements 
                    element.decompose()
                
                text = ' '.join(soup.stripped_strings)
                if not text or len(text) < 100:
                    raise ValueError("Insufficient text content")
                
                return text
                
            except Exception as e: # If an error occurs, print the error message and retry if there are more attempts left
                print(f"Attempt {attempt + 1} failed for {url}: {str(e)}")
                if attempt == max_retries - 1:
                    return None
                time.sleep(2 ** attempt) #retry with an exponential backoff 
