"""
LangChain Document Loader for Smart Markdown Web Scraper API (RapidAPI)
Seamlessly import cleaned web Markdown directly into LangChain Vector Stores (Chroma, FAISS, Pinecone).
"""

from typing import List, Optional
import requests
from langchain_core.documents import Document

class SmartMarkdownWebLoader:
    """
    LangChain Web Loader powered by Smart Markdown Web Scraper API on RapidAPI.
    URL: https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper
    """
    def __init__(self, urls: List[str], rapidapi_key: str):
        self.urls = urls
        self.rapidapi_key = rapidapi_key
        self.api_host = "smart-markdown-web-scraper.p.rapidapi.com"
        self.api_endpoint = f"https://{self.api_host}/scrape"

    def load(self) -> List[Document]:
        documents = []
        headers = {
            "x-rapidapi-key": self.rapidapi_key,
            "x-rapidapi-host": self.api_host,
            "Content-Type": "application/json"
        }

        for target_url in self.urls:
            try:
                response = requests.post(self.api_endpoint, json={"url": target_url}, headers=headers)
                response.raise_for_status()
                data = response.json()
                markdown_content = data.get("markdown", "")
                
                doc = Document(
                    page_content=markdown_content,
                    metadata={
                        "source": target_url,
                        "title": data.get("title", target_url),
                        "extractor": "SmartMarkdownWebScraper"
                    }
                )
                documents.append(doc)
            except Exception as e:
                print(f"Error loading {target_url}: {e}")

        return documents

# Quick Usage Example
if __name__ == "__main__":
    import os
    API_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
    loader = SmartMarkdownWebLoader(
        urls=["https://news.ycombinator.com", "https://techcrunch.com"],
        rapidapi_key=API_KEY
    )
    docs = loader.load()
    print(f"Loaded {len(docs)} documents successfully into LangChain format!")
    if docs:
        print("Sample snippet:\n", docs[0].page_content[:300])
