#1.	Create a new directory for the project:

mkdir seo_audit_tool
cd seo_audit_tool

#2.	Set up a virtual environment:

python -m venv venv

#3.	Activate the virtual environment:

source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows


#4.	Install necessary libraries:


pip install beautifulsoup4 requests lxml seaborn pandas matplotlib

#Now that the environment is set up, let's create a web scraper using BeautifulSoup and Requests to fetch the content of a given URL:

import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    else:
        raise Exception(f"Error fetching URL: {url}")

url = input("Enter the URL to analyze: ")
soup = fetch_website_content(url)
