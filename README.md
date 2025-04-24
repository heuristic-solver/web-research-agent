<p align="center">
  <h1>Web Research Agent</h1>
</p>

<p align="center">
  This is a Python-based smart research agent that automates the process of finding and summarizing information online for you.
</p>

<p align="center">
  <b>Try it live on Hugging Face:</b><br>
  <a href="https://huggingface.co/spaces/heuristic-solver/web_res_agent_joel">
    Web Research Agent on Hugging Face
  </a>
</p>

---

<p align="center">
  <h2>Installation and Setup</h2>
</p>

### 1. Clone this Repo

```bash
git clone https://github.com/heuristic-solver/web_research_agent.git
cd web_research_agent
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Up Configuration

You will need API keys for **SerpAPI** and **Gemini**:

- [SerpAPI](https://serpapi.com/)
- [Gemini API Key](https://aistudio.google.com/app/apikey)

Once you have them, update `config.py`:

```python
# config.py
SERPAPI_KEY = "YOUR_API_KEY"
GEMINI_KEY = "YOUR_API_KEY"
MAX_REQUESTS_PER_MINUTE = 2  # Rate Limits
REQUEST_DELAY = 30           # Delay between requests in seconds
```

### 4. Run the Application

```bash
python example_usage.py
```

---

<p align="center">
  <h2>File Overview</h2>
</p>

- **`config.py`** – Stores API keys and config settings.
- **`web_search.py`** – Handles web searches via SerpAPI.
- **`scraper.py`** – Scrapes and cleans web content.
- **`analyzer.py`** – Analyzes content using Gemini.
- **`example_usage.py`** – Sample interface to run the agent.
- **`agent.py`** – Core agent logic for combining all modules.

---

<p align="center">
  <h2>Troubleshooting</h2>
</p>

- Check your API keys in `config.py`.
- Ensure you have a working internet connection.
- Be aware of API rate limits or usage caps.

---

<p align="center">
  <h2>License</h2>
</p>

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
