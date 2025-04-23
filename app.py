import gradio as gr
from agent import WebResearchAgent
from config import SERPAPI_KEY, GEMINI_KEY

agent = WebResearchAgent(SERPAPI_KEY, GEMINI_KEY)

def run_research(query):
    result = agent.research(query)
    answer = result["answer"]
    sources = "\n".join([f"{src['title']} - {src['url']}" for src in result["sources"]])
    return answer, sources or "No sources found"

iface = gr.Interface(
    fn=run_research,
    inputs=gr.Textbox(label="Enter your research query"),
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Textbox(label="Sources")
    ],
    title="Web Research Agent",
    description="Ask a question"
)

if __name__ == "__main__":
    iface.launch()
