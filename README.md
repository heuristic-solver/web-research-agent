# Web Research Agent

This is a Python-based smart research agent that automates the process of finding and summarizing information online for you.

For no installation ease of use, try the agent out on Hugging Face:  
[Web Research Agent on Hugging Face](https://huggingface.co/spaces/heuristic-solver/web_res_agent_joel)

## Installation and Setup

### 1. Clone this Repo

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/heuristic-solver/web_research_agent.git
cd web_research_agent
```

### 2. Install Requirements

Install the required Python packages by running the following command:

```bash
pip install -r requirements.txt
```

### 3. Set Up Configuration

You will need API keys for **SerpAPI** and **Gemini**. Follow these steps to get the necessary API keys:

- **SerpAPI**: Create an account and get your API key from [SerpAPI](https://serpapi.com/).
- **Gemini**: Obtain your API key from [Google Cloud AI Studio](https://aistudio.google.com/app/apikey).

Once you have the required API keys, update them in the `config.py` file:

```python
# config.py
SERPAPI_KEY = "YOUR_API_KEY"
GEMINI_KEY = "YOUR_API_KEY"
MAX_REQUESTS_PER_MINUTE = 2  # Rate Limits
REQUEST_DELAY = 30  # Seconds between requests
```

### 4. Run the Application

To run this application, use the following command in the terminal:

```bash
python example_usage.py
```

---

## File Overview

- **`config.py`**: Configuration file for storing API keys and rate limits.
- **`web_search.py`**: Contains the `WebSearchTool` class for performing searches using SerpAPI.
- **`scraper.py`**: Contains the `WebScraper` class for scraping web page content.
- **`analyzer.py`**: Contains the `ContentAnalyzer` class for analyzing content with the Gemini model.
- **`example_usage.py`**: Example usage of the Web Research Agent, where you input queries and see results.
- **`agent.py`**: Contains the `WebResearchAgent` class, which combines the web search and content analysis functionalities.

## Troubleshooting

If you encounter issues:

- Ensure your API keys are correctly set in `config.py`.
- Make sure you have internet access to make requests to SerpAPI and Google Gemini.
- Check for any API rate limits or restrictions.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
