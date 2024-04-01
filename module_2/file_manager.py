"""
save_to_file saves the content of each article given the filename to be saved and the content to be saved to a text file in the processed data folder
save_HTML fetches raw HTML content from the given URL and saves it to a file in the raw data folder named by the given filename and index
each line is explained in comments throughout the code to show when and what is happening
"""

from abc import ABC, abstractmethod
import requests
import os

class FileSaver(ABC): #abstract base class that inherits from ABC
    @abstractmethod #any concrete class inheriting from this class must provide an implementation for this method
    def save(self, filename, content):
        pass

class FileManager(FileSaver):
    def __init__(self, raw_folder): #constructor method for initializing instances of FileManager
        self.raw_folder = raw_folder #initialize the raw_folder with the provided raw_folder parameter.

    def save_to_file(self, filename, content): #function to save the article to txt file
        with open(filename, 'w', encoding='utf-8') as file: #open given file for writing
            file.write(content) #write the content to the file

    def save_HTML(self, url, raw_folder, index): #function to save html content to the raw data folder
        try: #try to fetch the content from the url
            response = requests.get(url) #send a GET request to the url
            response.raise_for_status() #raise an exception for bad responses

            raw_filename = f'{raw_folder}/raw_html{index}.html' #name the file based on index
            with open(raw_filename, 'w', encoding='utf-8') as file: #open the raw file for writing
                file.write(response.text) #write all the content to the file

        except requests.exceptions.RequestException as e: #handle the exceptions from the request if necessary
            print(f"Couldn't access {url} to save raw HTML: {e}") #error message

    def save(self, filename, content):  #implementation for the abstract save method
        self.save_to_file(filename, content)