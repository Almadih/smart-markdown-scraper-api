#!/usr/bin/env python3
"""
Automated Cold Email Outreach Generator for AI & Scraping Developers.
Generates personalized outreach messages for target tech companies.
"""

import sys
import json

TARGET_LEADS = [
    {"name": "Alex", "company": "VectorSearch AI", "role": "Lead RAG Engineer", "email": "alex@example-ai.com"},
    {"name": "Sarah", "company": "AgentFlow", "role": "CTO", "email": "sarah@example-agent.io"},
    {"name": "David", "company": "DataCrawl Systems", "role": "Senior Scraping Engineer", "email": "david@example-data.com"}
]

EMAIL_TEMPLATE = """
Subject: Quick question about your RAG token costs at {company}

Hi {name},

I noticed you are leading engineering at {company} ({role}).

Most web scraping setups send raw HTML (with 4,000+ tokens of footer links, scripts, and ads) into LLM context windows, driving up OpenAI/Anthropic bills by 80%+.

We launched **Smart Markdown Web Scraper** on RapidAPI to solve this: it strips DOM noise and returns clean, structured Markdown in <300ms.

You can try 100 free requests/mo here: https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper

Happy to send over a custom test key with 10k credits if you'd like to benchmark it against your current parser!

Best regards,
Modi Almadih
"""

def generate_campaign():
    print("📧 Generated Personalized Cold Outreach Emails:\n" + "="*50)
    for lead in TARGET_LEADS:
        email_body = EMAIL_TEMPLATE.format(
            name=lead["name"],
            company=lead["company"],
            role=lead["role"]
        )
        print(f"\n📩 TO: {lead['email']} ({lead['name']} - {lead['company']})")
        print(email_body.strip())
        print("-" * 50)

if __name__ == "__main__":
    generate_campaign()
