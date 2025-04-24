<div align="center">
  <h1>Web Research Agent</h1>
</div>

This is a Python-based smart research agent that automates the process of finding and summarizing information online for you.
![image](https://github.com/user-attachments/assets/552e06e3-da51-4192-b799-3cedac8ad1af)


For no installation ease of use, try the agent out on Hugging Face:  
[Web Research Agent on Hugging Face](https://huggingface.co/spaces/heuristic-solver/web_res_agent_joel)

---

<div align="center">
  <h2>Installation and Setup</h2>
</div>

### 1. Clone this Repo

```bash
git clone https://github.com/heuristic-solver/web_research_agent.git
cd web_research_agent
```

### 2. Install Requirements

Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### 3. Set Up Configuration

You will need API keys for **SerpAPI** and **Gemini**:

- [SerpAPI](https://serpapi.com/)
- [Gemini API Key](https://aistudio.google.com/app/apikey)

Once you have the keys, update `config.py`:

```python
# config.py
SERPAPI_KEY = "YOUR_API_KEY"
GEMINI_KEY = "YOUR_API_KEY"
MAX_REQUESTS_PER_MINUTE = 2
REQUEST_DELAY = 30
```

### 4. Run the Application

To run this application, use the following command in the terminal:

```bash
python example_usage.py
```

---

<div align="center">
  <h2>File Overview</h2>
</div>

- **`config.py`** – Stores API keys and rate limit configuration.
- **`web_search.py`** – Performs searches using SerpAPI.
- **`scraper.py`** – Scrapes and cleans website content.
- **`analyzer.py`** – Analyzes web content using the Gemini model.
- **`example_usage.py`** – Sample interface to run the agent via CLI.
- **`agent.py`** – Core logic that integrates search, scrape, and analysis.

---

<div align="center">
  <h2>Troubleshooting</h2>
</div>

- Ensure your API keys are correct in `config.py`.
- Make sure your internet connection is active.
- Check for rate limits on your SerpAPI or Gemini usage.

---

<div align="center">

