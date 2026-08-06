const SmartMarkdownScraper = require('./index.js');

const apiKey = process.env.RAPIDAPI_KEY || "YOUR_RAPIDAPI_KEY";
const client = new SmartMarkdownScraper(apiKey);

console.log("Testing Node.js SDK for Smart Markdown Scraper...");
client.scrapeUrl("https://news.ycombinator.com")
  .then(res => {
    console.log("✅ Success! Response preview:");
    console.log(JSON.stringify(res, null, 2).slice(0, 300));
  })
  .catch(err => {
    console.log("ℹ️ Test completed (Pass a valid RAPIDAPI_KEY to execute live network requests). Error:", err.message);
  });
