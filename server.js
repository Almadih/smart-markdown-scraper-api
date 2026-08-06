const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const axios = require('axios');
const { JSDOM } = require('jsdom');
const { Readability } = require('@mozilla/readability');
const TurndownService = require('turndown');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Security and Middleware
app.use(helmet({
  contentSecurityPolicy: false // Allow inline scripts for demo playground
}));
app.use(cors());
app.use(express.json());

// Serve Static Landing Page & Playground from landing-page/
app.use(express.static(path.join(__dirname, 'landing-page')));

// Trust proxy for rate limiting behind reverse proxy (Nginx/Cloudflare)
app.set('trust proxy', 1);

// Basic Rate Limiter
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 200, // Limit each IP to 200 requests per window
  message: { error: 'Too many requests, please try again later.' }
});
app.use(limiter);

// Setup Turndown for converting HTML to clean Markdown
const turndownService = new TurndownService({
  headingStyle: 'atx',
  hr: '---',
  bullet: '*',
  codeBlockStyle: 'fenced'
});

turndownService.remove(['script', 'style', 'iframe', 'noscript', 'svg']);

turndownService.addRule('keepImages', {
  filter: 'img',
  replacement: (content, node) => {
    const alt = node.getAttribute('alt') || '';
    const src = node.getAttribute('src') || '';
    return src ? `![${alt}](${src})` : '';
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date() });
});

// Main Reader Core Function
async function handleScrape(targetUrl, res) {
  if (!targetUrl) {
    return res.status(400).json({ error: 'Missing required parameter "url"' });
  }

  try {
    const parsedUrl = new URL(targetUrl);
    if (!['http:', 'https:'].includes(parsedUrl.protocol)) {
      return res.status(400).json({ error: 'Invalid URL protocol. Only HTTP and HTTPS are supported.' });
    }

    const response = await axios.get(targetUrl, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
      },
      timeout: 15000
    });

    const html = response.data;
    const dom = new JSDOM(html, { url: targetUrl });
    const reader = new Readability(dom.window.document);
    const article = reader.parse();

    if (!article) {
      return res.status(422).json({ error: 'Failed to extract readable content from this page.' });
    }

    const markdown = turndownService.turndown(article.content);

    res.json({
      title: article.title,
      byline: article.byline || null,
      siteName: article.siteName || null,
      length: article.length || 0,
      url: targetUrl,
      markdown: markdown
    });

  } catch (error) {
    console.error(`Error processing URL ${targetUrl}:`, error.message);
    if (error.response) {
      return res.status(error.response.status).json({
        error: `Target server responded with status code ${error.response.status}`,
        details: error.response.statusText
      });
    }
    res.status(500).json({ error: 'An error occurred while processing the request.', details: error.message });
  }
}

// Endpoints for /scrape and /read
app.all(['/scrape', '/read'], (req, res) => {
  const targetUrl = req.query.url || (req.body && req.body.url);
  handleScrape(targetUrl, res);
});

app.listen(PORT, () => {
  console.log(`⚡ Smart Markdown Web Scraper Server running on http://localhost:${PORT}`);
});
