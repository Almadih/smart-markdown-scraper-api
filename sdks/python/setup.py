from setuptools import setup, find_packages

setup(
    name="smart-markdown-scraper",
    version="1.0.0",
    description="Python SDK for Smart Markdown Web Scraper API on RapidAPI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Modi Almadih",
    url="https://rapidapi.com/modialmadih/api/smart-markdown-web-scraper",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.7",
)
