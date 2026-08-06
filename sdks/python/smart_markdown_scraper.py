import requests
from typing import Dict, Any, Optional

class SmartMarkdownScraper:
    """
    Python SDK for Smart Markdown Web Scraper API hosted on RapidAPI.
    Converts any web URL into clean, structured Markdown for LLMs and RAG pipelines.
    """
    DEFAULT_HOST = "smart-markdown-web-scraper.p.rapidapi.com"

    def __init__(self, rapidapi_key: str, api_host: Optional[str] = None):
        """
        Initialize the SDK with your RapidAPI Key.
        :param rapidapi_key: Your RapidAPI secret key (X-RapidAPI-Key)
        """
        if not rapidapi_key:
            raise ValueError("RapidAPI key is required. Get one at https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper")
        
        self.rapidapi_key = rapidapi_key
        self.api_host = api_host or self.DEFAULT_HOST
        self.base_url = f"https://{self.api_host}"

    def scrape_url(self, target_url: str, custom_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Scrape a target URL and convert its main body into clean Markdown.
        
        :param target_url: The full HTTP/HTTPS URL of the page to scrape.
        :param custom_headers: Optional headers to pass to the request.
        :return: Dict containing 'markdown', 'title', 'status', and metadata.
        """
        endpoint = f"{self.base_url}/scrape"
        
        headers = {
            "x-rapidapi-key": self.rapidapi_key,
            "x-rapidapi-host": self.api_host,
            "Content-Type": "application/json"
        }
        
        payload = {
            "url": target_url
        }

        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

# Example Usage
if __name__ == "__main__":
    import os
    API_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY_HERE")
    
    scraper = SmartMarkdownScraper(rapidapi_key=API_KEY)
    try:
        result = scraper.scrape_url("https://news.ycombinator.com")
        print("--- Scraped Markdown ---")
        print(result.get("markdown", result))
    except Exception as e:
        print(f"Error scraping URL: {e}")
