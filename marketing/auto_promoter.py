#!/usr/bin/env python3
"""
Automated Social & Dev Community Article Publisher
Publishes marketing articles directly to Dev.to API.
"""

import os
import sys
import requests
import json

DEVTO_API_URL = "https://dev.to/api/articles"

ARTICLES = [
    {
        "title": "Why HTML Scraping Fails for LLMs (And How to Extract Clean Markdown in 3 Lines of Code)",
        "published": True,
        "tags": ["python", "ai", "webscraping", "openai"],
        "body_markdown": """
If you've built any RAG (Retrieval-Augmented Generation) system or AI Agent recently, you know the nightmare of web scraping:

Raw HTML is filled with <div> tags, inline scripts, navigation menus, tracking pixels, and ads. Passing raw HTML into GPT-4 or Claude 3.5 wastes **up to 85% of your context window** on useless boilerplate.

### The Solution: Web to Markdown Conversion

By converting web pages directly into clean, semantic Markdown before feeding them into your vector database or LLM, you:
1. **Reduce Prompt Costs**: Save 80%+ on API token usage.
2. **Improve Accuracy**: Remove distracting layout elements so the LLM focuses purely on main article content.
3. **Speed Up Retrieval**: Chunk clean markdown headings (`#`, `##`) cleanly into vector stores.

### Quick 3-Line Python Implementation

Using the **Smart Markdown Web Scraper API** on RapidAPI:

```python
import requests

url = "https://smart-markdown-web-scraper.p.rapidapi.com/scrape"
payload = { "url": "https://news.ycombinator.com" }
headers = {
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
    "x-rapidapi-host": "smart-markdown-web-scraper.p.rapidapi.com",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
markdown_content = response.json()["markdown"]

print(markdown_content)
```

👉 **Get your API Key & Try 100 Free Requests/Month**: [Smart Markdown Web Scraper on RapidAPI](https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper)
"""
    },
    {
        "title": "How to Build an Autonomous AI Web Research Agent with CrewAI & Smart Markdown API",
        "published": True,
        "tags": ["python", "ai", "aiagents", "rag"],
        "body_markdown": """
When building autonomous AI agents (like CrewAI, AutoGen, or LangGraph) that search and read web documentation, feeding raw HTML causes context truncation errors.

Here is how to equip your CrewAI agent with clean Markdown scraping:

### Step 1: Install Dependencies
```bash
pip install crewai requests
```

### Step 2: Define the Scraping Tool
```python
import requests
from crewai.tools import tool

@tool("Smart Web Scraper")
def scrape_webpage(url: str) -> str:
    \"\"\"Scrapes a URL and returns clean Markdown optimized for LLMs.\"\"\"
    endpoint = "https://smart-markdown-web-scraper.p.rapidapi.com/scrape"
    headers = {
        "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
        "x-rapidapi-host": "smart-markdown-web-scraper.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response = requests.post(endpoint, json={"url": url}, headers=headers)
    return response.json().get("markdown", "")
```

### Step 3: Run Your AI Agent
Now your CrewAI researcher can read technical documentation sites or news articles with zero HTML noise!

👉 **Try the API on RapidAPI Hub**: [Smart Markdown Web Scraper](https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper)
"""
    }
]

def publish_articles(api_key: str):
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }
    for idx, article in enumerate(ARTICLES, 1):
        print(f"🚀 Publishing Article #{idx}: {article['title']}...")
        payload = {"article": article}
        res = requests.post(DEVTO_API_URL, json=payload, headers=headers)
        if res.status_code == 201:
            data = res.json()
            print(f"✅ Published Article #{idx} successfully! URL: {data.get('url')}\n")
        else:
            print(f"⚠️ Warning/Error ({res.status_code}): {res.text}\n")

def main():
    devto_key = os.getenv("DEVTO_API_KEY")
    if devto_key:
        publish_articles(devto_key)
    else:
        print("💡 DEVTO_API_KEY environment variable not set.")

if __name__ == "__main__":
    main()
