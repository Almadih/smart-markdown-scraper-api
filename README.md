# 🚀 Smart Markdown Web Scraper API - Growth & Ecosystem Hub

> Official project repository for **Smart Markdown Web Scraper API** hosted on [RapidAPI](https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper).
> Includes SDKs, framework integrations, Chrome Extension, interactive landing page, and full marketing growth kits.

👉 **Live Demo & Playground**: [https://almadih.github.io/smart-markdown-web-scraper-api/](https://almadih.github.io/smart-markdown-web-scraper-api/)

---

## 📂 Repository Structure

```
scraper-api/
├── README.md                      # Primary project Hub documentation
├── landing-page/                  # Interactive Web Playground & Marketing Site
│   ├── index.html
│   ├── style.css
│   └── app.js
├── sdks/                          # Official Client Libraries
│   ├── python/                    # Python SDK (`smart_markdown_scraper.py`)
│   └── nodejs/                    # Node.js SDK (`index.js`)
├── integrations/                  # AI Framework Connectors
│   ├── langchain_loader.py        # LangChain Document Loader integration
│   └── llamaindex_reader.py       # LlamaIndex Document Reader integration
├── cli/                           # Command Line Interface Tool
│   └── smart_md.py                # Terminal tool (`smart-md`)
├── chrome-extension/              # Browser Extension (Manifest V3)
│   ├── manifest.json              # Extension manifest
│   ├── popup.html                 # Popup interface
│   └── popup.js                   # API caller & clipboard logic
└── .github/workflows/             # GitHub CI/CD Workflows
    └── deploy-pages.yml           # Auto-deploys landing-page to GitHub Pages
```

---

## 🚀 Quick Usage Summaries

### 1. Python SDK (`sdks/python/`)
```python
from sdks.python.smart_markdown_scraper import SmartMarkdownScraper

client = SmartMarkdownScraper(rapidapi_key="YOUR_RAPIDAPI_KEY")
res = client.scrape_url("https://news.ycombinator.com")
print(res["markdown"])
```

### 2. Command Line Tool (`cli/`)
```bash
python cli/smart_md.py https://techcrunch.com --key YOUR_RAPIDAPI_KEY -o output.md
```

### 3. LangChain Vector Loader (`integrations/`)
```python
from integrations.langchain_loader import SmartMarkdownWebLoader

loader = SmartMarkdownWebLoader(urls=["https://example.com"], rapidapi_key="YOUR_KEY")
docs = loader.load()
```

---

## 🔗 Key Links
- **Live Interactive Playground**: [https://almadih.github.io/smart-markdown-scraper-api/](https://almadih.github.io/smart-markdown-web-scraper-api/)
- **RapidAPI Hub Page**: [https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper](https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper)
- **Dev.to Tutorial**: [Why HTML Scraping Fails for LLMs](https://dev.to/almadih/why-html-scraping-fails-for-llms-and-how-to-extract-clean-markdown-in-3-lines-of-code-3op8)
