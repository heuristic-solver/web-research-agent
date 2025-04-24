import json
import time
from datetime import datetime
from typing import List, Dict
from tools.web_search import WebSearchTool
from tools.scraper import WebScraper
from tools.analyzer import ContentAnalyzer

class WebResearchAgent:
    #initialize the agent with API Keys
    def __init__(self, search_api_key: str, gemini_api_key: str):
        self.search_tool = WebSearchTool(search_api_key)
        self.scraper = WebScraper()
        self.analyzer = ContentAnalyzer(gemini_api_key)
        self.cache = {}
    #performs web search, scraping analysis 
    def research(self, query: str) -> Dict:
        try:
            search_terms = self._analyze_query(query) #used to analyze the query to obtain search terms
            if not search_terms:
                return self._empty_response(query, "Could not analyze query")
            
            search_results = self.search_tool.search(search_terms) #perform search with relevant search terms
            if not search_results:
                return self._empty_response(query, "No search results found")
            
            research_data = [] #list to store analyzed content 
            fallback_data = [] #list to store results in case analysis fails 
            
            for result in search_results[:3]: #Go through top 3 URL's 
                url = result.get('link')
                if not url:
                    continue
                    
                content = self._get_content(url)
                if not content:
                    continue
                    
                try: #content analysis 
                    analysis = self.analyzer.analyze(content, query)
                    research_data.append({
                        'url': url,
                        'title': result.get('title', 'No title'),
                        'content': content[:1000],
                        'analysis': analysis
                    })
                except Exception as e: # If analysis fails, store fallback data without analysis
                    fallback_data.append({
                        'url': url,
                        'title': result.get('title', 'No title'),
                        'content': content[:1000]
                    })
                
                time.sleep(1) # Adding delay to prevent overwhelming the server with requests
            # If no successful analysis, fallback with basic content information
            if not research_data and fallback_data:
                research_data = [{
                    **item,
                    'analysis': {
                        'relevance_score': 6,
                        'key_points': ["Content available but not analyzed"],
                        'summary': item['content'][:200] + "..."
                    }
                } for item in fallback_data]
            
            if research_data: # If data exists, synthesize results into a comprehensive response
                return self._synthesize_results(query, research_data)
            return self._empty_response(query, "No valid content could be processed")
            
        except Exception as e:
            print(f"Research error at {datetime.now()}: {str(e)}")
            return self._empty_response(query, f"Research failed: {str(e)}")
    
    def _analyze_query(self, query: str) -> str:
        query_lower = query.lower()
        
        if any(word in query_lower for word in ["population", "demographics"]):
            return f"{query} site:worldpopulationreview.com OR site:worldometers.info"
        
        if any(word in query_lower for word in ["technology", "AI", "artificial intelligence"]):
            return f"{query} site:arxiv.org OR site:techcrunch.com"
        
        return query
    
    def _get_content(self, url: str) -> str:
        if url in self.cache:
            return self.cache[url]
        
        content = self.scraper.scrape(url)
        if content:
            self.cache[url] = content
        return content
    
    def _synthesize_results(self, query: str, data: List[Dict]) -> Dict:
        context = "\n\n".join(
            f"Source {i+1} ({d['url']}):\n"
            f"Relevance: {d['analysis']['relevance_score']}/10\n"
            f"Summary: {d['analysis']['summary']}"
            for i, d in enumerate(data)
        )
        
        prompt = f"""Research Question: {query}
        
        Sources:
        {context}
        
        Compose a comprehensive answer with:
        1. Direct answer
        2. Supporting evidence
        3. Source citations"""
        
        response = self.analyzer.model.generate_content(prompt)
        return {
            'query': query,
            'answer': response.text,
            'sources': [{'url': d['url'], 'title': d['title']} for d in data]
        }
    
    def _empty_response(self, query: str, message: str) -> Dict:
        return {
            'query': query,
            'answer': message,
            'sources': []
        }
