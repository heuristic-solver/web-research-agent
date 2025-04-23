import requests

class WebSearchTool:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://serpapi.com/search.json"
    
    def search(self, query, num_results=5):
        params = {
            "q": query,
            "api_key": self.api_key,
            "num": num_results
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get("organic_results", [])
        except requests.exceptions.RequestException as e:
            print(f"Search failed: {str(e)}")
            return []