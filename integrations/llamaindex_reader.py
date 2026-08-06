"""
LlamaIndex Custom Reader for Smart Markdown Web Scraper API (RapidAPI)
Ingest clean web Markdown directly into LlamaIndex VectorStoreIndex.
"""

from typing import List, Optional
import requests
from llama_index.core.schema import Document

class SmartMarkdownReader:
    """
    LlamaIndex Data Reader powered by Smart Markdown Web Scraper API on RapidAPI.
    URL: https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper
    """
    def __init__(self, rapidapi_key: str):
        self.rapidapi_key = rapidapi_key
        self.api_host = "smart-markdown-web-scraper.p.rapidapi.com"
        self.api_endpoint = f"https://{self.api_host}/scrape"

    def load_data(self, urls: List[str]) -> List[Document]:
        """
        Load web pages as LlamaIndex Document objects.
        :param urls: List of target web page URLs
        :return: List of LlamaIndex Document objects
        """
        documents = []
        headers = {
            "x-rapidapi-key": self.rapidapi_key,
            "x-rapidapi-host": self.api_host,
            "Content-Type": "application/json"
        }

        for url in urls:
            try:
                res = requests.post(self.api_endpoint, json={"url": url}, headers=headers)
                res.raise_for_status()
                data = res.json()
                markdown_text = data.get("markdown", "")

                doc = Document(
                    text=markdown_text,
                    metadata={
                        "url": url,
                        "title": data.get("title", url),
                        "source": "SmartMarkdownWebScraper"
                    }
                )
                documents.append(doc)
            except Exception as e:
                print(f"Error loading {url}: {e}")

        return documents

# Example Usage
if __name__ == "__main__":
    import os
    reader = SmartMarkdownReader(rapidapi_key=os.getenv("RAPIDAPI_KEY", "YOUR_KEY"))
    docs = reader.load_data(["https://news.ycombinator.com"])
    print(f"Loaded {len(docs)} document into LlamaIndex!")
