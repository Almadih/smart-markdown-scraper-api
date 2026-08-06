/**
 * Smart Markdown Web Scraper Node.js Client
 * Powered by RapidAPI (https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper)
 */

class SmartMarkdownScraper {
  constructor(rapidApiKey, options = {}) {
    if (!rapidApiKey) {
      throw new Error("RapidAPI key is required. Get one at https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper");
    }
    this.rapidApiKey = rapidApiKey;
    this.apiHost = options.apiHost || "smart-markdown-web-scraper.p.rapidapi.com";
    this.baseUrl = `https://${this.apiHost}`;
  }

  async scrapeUrl(targetUrl) {
    const endpoint = `${this.baseUrl}/scrape`;

    const response = await fetch(endpoint, {
      method: "POST",
      headers: {
        "x-rapidapi-key": this.rapidApiKey,
        "x-rapidapi-host": this.apiHost,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url: targetUrl }),
    });

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(`RapidAPI Request failed (${response.status}): ${errText}`);
    }

    return await response.json();
  }
}

module.exports = SmartMarkdownScraper;
