# Smart Markdown Web Scraper - Node.js SDK ⚡

> Convert web pages into clean, structured Markdown for **LLMs**, **LangChain**, and **AI Agents**. Powered by [RapidAPI](https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper).

## 🚀 Quick Install

```bash
npm install smart-markdown-scraper
```

## 💻 Usage

```javascript
const SmartMarkdownScraper = require('smart-markdown-scraper');

const client = new SmartMarkdownScraper('YOUR_RAPIDAPI_KEY');

async function run() {
  const result = await client.scrapeUrl('https://news.ycombinator.com');
  console.log(result.markdown);
}

run();
```

## 📖 API Documentation & Key
Get your API Key & test online at [RapidAPI Hub](https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper).
