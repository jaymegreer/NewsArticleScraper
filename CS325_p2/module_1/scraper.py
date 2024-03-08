# this module extracts text content from a given URL and outputs it to a plain text file
# it extracts the main article content from the div with the class='article-body__content'. 
# once all is retrieved, it converts the HTML content from the page to regular text and saves
# each of the extracted article's data to individual text files named article1-article5.
# each line is explained in comments throughout the code to show when and what is happening

import requests 
from bs4 import BeautifulSoup
import html2text
from abc import ABC, abstractmethod


class ContentExtractor(ABC):  #abstract base class that inherits from ABC
    @abstractmethod #any concrete class inheriting from this class must provide an implementation for this method
    def extract_content(self, url):
        pass

class Scraper(ContentExtractor):
    def __init__(self): #constructor method for initializing instances of Scraper
        pass

    def extract_content(self, url): #function to extract content from URL
        try:
            response = requests.get(url) #send GET request to url
            response.raise_for_status() #raise an exception for bad requests

            parsed_content = BeautifulSoup(response.text, 'html.parser') #parse the content using BeautifulSoup
            article_content = parsed_content.find('div', {'class': 'article-body__content'}) #find article content

            converted_text = html2text.HTML2Text() #creates an instance of HTML2Text class for converting
            converted_text.ignore_links = True #ignore links just get the text
            article_text = converted_text.handle(str(article_content)) #converts html to plain text using the instance

            return article_text #return extracted and converted content
    
        except requests.exceptions.RequestException as e: #catch bad requests
            print(f"Couldn't access {url}: {e}") #error message
            return None
    