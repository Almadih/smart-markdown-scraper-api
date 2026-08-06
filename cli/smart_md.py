#!/usr/bin/env python3
"""
Smart Markdown CLI (smart-md)
Convert any web page URL to clean, LLM-ready Markdown from your command line terminal.
Powered by RapidAPI: https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper
"""

import argparse
import sys
import os
import requests

DEFAULT_HOST = "smart-markdown-web-scraper.p.rapidapi.com"

def main():
    parser = argparse.ArgumentParser(description="Convert web URLs to clean Markdown for LLMs & AI agents.")
    parser.add_argument("url", help="Target URL to scrape (e.g. https://example.com/article)")
    parser.add_argument("-k", "--key", help="RapidAPI Key (or set RAPIDAPI_KEY env var)")
    parser.add_argument("-o", "--output", help="Output file path (default: stdout)")
    
    args = parser.parse_args()
    
    api_key = args.key or os.getenv("RAPIDAPI_KEY")
    if not api_key:
        print("❌ Error: Missing RapidAPI key. Pass --key or set RAPIDAPI_KEY environment variable.", file=sys.stderr)
        print("Get your free key at: https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper", file=sys.stderr)
        sys.exit(1)

    url = f"https://{DEFAULT_HOST}/scrape"
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": DEFAULT_HOST,
        "Content-Type": "application/json"
    }

    print(f"⚡ Scraping {args.url} via Smart Markdown API...", file=sys.stderr)
    
    try:
        res = requests.post(url, json={"url": args.url}, headers=headers)
        res.raise_for_status()
        data = res.json()
        markdown = data.get("markdown", str(data))

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"✅ Saved Markdown output to {args.output}", file=sys.stderr)
        else:
            print(markdown)

    except Exception as e:
        print(f"❌ Scraping failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
