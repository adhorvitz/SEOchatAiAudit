# Text Parser Module (text_parser.py). This module processes and organizes the extracted data for further analysis.

import re

class TextParser:
    def __init__(self, data):
        self.data = data

    def clean_text(self, text):
        # Remove HTML tags, special characters, and extra whitespace
        cleaned_text = re.sub(r'<[^>]*>', ' ', text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        cleaned_text = re.sub(r'[^\x00-\x7F]+', ' ', cleaned_text)
        cleaned_text = cleaned_text.strip()

        return cleaned_text

    def parse(self):
        parsed_data = {
            "title": self.clean_text(self.data["title"]),
            "meta_description": self.clean_text(self.data["meta_description"]) if self.data["meta_description"] else None,
            "header_tags": [(tag, self.clean_text(text)) for tag, text in self.data["header_tags"]],
            "content": self.clean_text(self.data["content"]),
            "links": self.data["links"]
        }

        return parsed_data

# The TextParser class takes the extracted data from the Web Scraper Module and processes it by cleaning the text (removing HTML tags, special characters, and extra whitespace) using the clean_text method. The parse method returns the cleaned and organized data.
