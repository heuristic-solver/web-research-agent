from agent import WebResearchAgent
from config import SERPAPI_KEY, GEMINI_KEY
import textwrap

def display_results(result):
    """Pretty-print results"""
    print(f"\n{'='*50}\nQUERY: {result['query']}\n{'='*50}")
    print("\nRESULT:")
    print(textwrap.fill(result['answer'], width=80))
    
    if result['sources']: #if results are found, print the sources 
        print("\nSOURCES:")
        for src in result['sources']:
            print(f"- {src['title']}\n  {src['url']}")
    else:
        print("\nNo sources available")

def main():
    agent = WebResearchAgent(SERPAPI_KEY, GEMINI_KEY) #initialize the research agent with given keys 
    
    print("Web Research Agent (using Gemini 1.5)")
    while True:
        query = input("\nEnter research query (or 'quit'): ").strip()
        if query.lower() in ('quit', 'exit'): #logic for user to exit 
            break
            
        print("\nResearching...")
        result = agent.research(query)
        display_results(result)

if __name__ == "__main__":
    main()
