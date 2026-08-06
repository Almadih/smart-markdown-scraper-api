# Smart Markdown Web Scraper - Python SDK 🚀

> Convert any webpage into clean, structured Markdown for **LLMs**, **RAG pipelines**, and **AI Agents** in 1 line of Python code. Powered by [RapidAPI](https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper).

## 🚀 Features
- 🧹 **Noise-Free Markdown**: Strips ads, navigation headers, footers, and tracking scripts.
- ⚡ **LLM Optimized**: Reduces token consumption by up to 85% compared to raw HTML.
- 🔑 **RapidAPI Powered**: Easy integration with enterprise-grade reliability and rate limiting.

## 📦 Installation

```bash
pip install requests
```

## 💡 Quick Start

```python
from smart_markdown_scraper import SmartMarkdownScraper

# Initialize with your RapidAPI Key
scraper = SmartMarkdownScraper(rapidapi_key="YOUR_RAPIDAPI_KEY")

# Scrape any URL
result = scraper.scrape_url("https://techcrunch.com")

# Access the cleaned markdown output
print(result["markdown"])
```

## 🔗 Useful Links
- [Get your API Key on RapidAPI](https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper)
- [Live Demo & Playground](https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper)
