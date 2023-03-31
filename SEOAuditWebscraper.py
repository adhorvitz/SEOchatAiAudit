# The WebScraper class is responsible for fetching and extracting relevant data from a given URL. The scrape method fetches the page content and extracts the relevant data (e.g., page title, meta description, header tags, content, and links) using helper methods.
#Web Scraper Module (web_scraper.py). We'll use the requests library to fetch the page content and BeautifulSoup from the bs4 library to parse the HTML content.

import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_page_content(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch the content for {self.url}. Status code: {response.status_code}")

    def extract_data(self, content):
        soup = BeautifulSoup(content, "html.parser")

        # Extract relevant data, e.g., page title, meta description, header tags, content, and links
        data = {
            "title": self.extract_title(soup),
            "meta_description": self.extract_meta_description(soup),
            "header_tags": self.extract_header_tags(soup),
            "content": self.extract_content(soup),
            "links": self.extract_links(soup)
        }

        return data

    def extract_title(self, soup):
        return soup.title.string

    def extract_meta_description(self, soup):
        meta_description = soup.find("meta", {"name": "description"})
        return meta_description["content"] if meta_description else None

    def extract_header_tags(self, soup):
        header_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
        headers = []

        for tag in header_tags:
            headers.extend([(header.name, header.text) for header in soup.find_all(tag)])

        return headers

    def extract_content(self, soup):
        # You can customize this function to extract content based on the structure of the website
        content_tag = soup.find("body")
        return content_tag.text if content_tag else None

    def extract_links(self, soup):
        return [link["href"] for link in soup.find_all("a", href=True)]

    def scrape(self):
        content = self.fetch_page_content()
        data = self.extract_data(content)

        return data
