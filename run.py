"""
first, this main function creates the folders "data/raw" and "data/processed" if they don't exist
then reads URLs from the file "websiteURLs.txt", and saves the raw HTML content using the save_HTML function, 
which is explained in module_2, and then extracts the content using the extract_content function, which is explained in module_1. 
With the extracted data, it then saves the content into the processed folder using the save_to_file function explained in module_1.
each line is explained in comments throughout the code to show when and what is happening

SOLID principle used: Open-Closed Principle (seen in file_manager.py and scraper.py) - 
This principle allows the functionality of this program to be extended without modifying the code
So now new classes that adhere to the FileSaver class in file_manager.py or ContentExtractor class in scraper.py 
can be introduced, which could add other ways to save a file or extract data without changing the current methods used
this can overall help with bugs since there will be less of a risk of adding bugs by modifying alreayd working code, so
the new code can be tested independently from what is working. This also makes the code more stable and able to be scaled up
new features can be added and the working code remains stable, so adding new stuff is easier meaning this program's scalability is maintainable
"""

import os   #allows code to interact with os (used to make directories)
from module_1.scraper import Scraper, ContentExtractor
from module_2.file_manager import FileManager, FileSaver
from module_3.AI_summarizer import connect_to_gemini_api, send_prompt_to_llm

def main():
    #define paths for the data folders
    raw_folder = "data/raw"
    processed_folder = "data/processed"

    #create the folders if they dont exist
    os.makedirs(raw_folder, exist_ok=True)
    os.makedirs(processed_folder, exist_ok=True)

    with open('websiteURLs.txt', 'r') as file: #open the file that contains the urls
        urls = file.read().splitlines() #read urls from the txt file and store them in a list

    #Load API key for Gemini
    api_key = 'ADD YOUR OWN KEY' #load your own API key 
    connect_to_gemini_api(api_key) #configure gemini based on given key
    
    #create instances of FileManager class and the Scraper class in order to use its methods
    file_manager = FileManager(raw_folder)
    scraper = Scraper()

    for i, url in enumerate(urls, start=1): #process each url
        file_manager.save_HTML(url, raw_folder, i) #save the raw html content 

        article_content, article_title = scraper.extract_content(url) #extract the article content and title

        if article_content: #check if the article content was correctly extracted
            prompt = "Please make the article concise, up to 50 words, the article is: " #prompt for ai to generate summary
            concise_article = send_prompt_to_llm(prompt, article_content) #call function to get summary/concise article
            output_article = f"Title: {article_title}\n\nSummary: \n{concise_article}\n\nFull Article: \n{article_content}" #layout of how i want the output to be
            output_filename = f'{processed_folder}/{article_title}.txt' #filename based on article name
            file_manager.save_to_file(output_filename, output_article) #save scraped articles to new text file
        else: #print error message
            print(f'Failed to extract content for article {i}') #error

if __name__ == "__main__":
    main()

