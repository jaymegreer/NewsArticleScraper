import requests 
from bs4 import BeautifulSoup
import html2text

def extractContent(url): #function to extract content from URL
    try:
        response = requests.get(url) #send request to url
        response.raise_for_status() #raise an exception for bad requests

        parsedContent = BeautifulSoup(response.text, 'html.parser') #parse the content

        articleContent = parsedContent.find('div', {'class': 'article-body__content'}) #find article content

        convertedText = html2text.HTML2Text() #convert html to normal text
        convertedText.ignore_links = True
        articleText = convertedText.handle(str(articleContent))

        return articleText
    
    except requests.exceptions.RequestException as e: #catch bad requests
        print(f"Couldn't access {url}: {e}")
        return None
    
def saveToFile(filename, content): #function to save the article to txt file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

with open('websiteURLs.txt', 'r') as file: #read urls from my txt file
    urls = file.read().splitlines()

for i, url in enumerate(urls, start=1): #process each url
    articleContent = extractContent(url)

    if articleContent:
        saveToFile(f'article{i}.txt', articleContent) #save scraped articles to new text file
    else:
        print(f'Failed to extract content for article {i}') #error
    

