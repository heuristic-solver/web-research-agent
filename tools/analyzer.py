import google.generativeai as genai
import json
import time
from config import REQUEST_DELAY

class ContentAnalyzer:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')
        self.last_request_time = 0
    
    def _rate_limit(self):
        elapsed = time.time() - self.last_request_time
        if elapsed < REQUEST_DELAY:
            time.sleep(REQUEST_DELAY - elapsed)
        self.last_request_time = time.time()
    
    def analyze(self, text, query):
        self._rate_limit()
        
        prompt = f"""Analyze this text for relevance to: '{query}'
        
        Return ONLY a JSON object with these keys:
        - "relevance_score" (1-10)
        - "key_points" (array of strings)
        - "summary" (string)
        
        Text: {text[:3000]}"""
        
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={"temperature": 0.2}
            )
            
            response_text = response.text.strip()
            if response_text.startswith('```json'):
                response_text = response_text[7:-3].strip()
            
            return json.loads(response_text)
            
        except Exception as e:
            print(f"Analysis failed for query '{query}': {str(e)}")
            return {
                "relevance_score": 5,
                "key_points": ["Analysis unavailable"],
                "summary": "Could not analyze content"
            }