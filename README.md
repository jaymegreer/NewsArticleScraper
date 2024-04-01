# Project 1
# Jayme Greer

## What the Program Does:
This Python program is designed to scrap news articles and summarize them from a list of URLs provided in the text file 'websiteURLs.txt', and I chose all entertainment article types. The program uses the 'requests', 'beautifulsoup4', and 'html2text' libraries to extract the main article content and save it to separate text files. It also used 'google.generativeai' to summarize the articles in 50 words or under using Google's AI. Comments in the code is added to describe as much as possible.
- It does all this by 
    - visits each URL from the provided text file
    - saves the raw html files into the raw data folder 
    - extracts the main article content and title from the div with the class 'article-body__content' and 'article-hero-headline__htag', respectively
    - converts the HTML content from the page to regular text
    - summarizes the article given the prompt and extracted article content using ai
    - saves each of the article's titles, summaries, and extracted data to individual text files named based on their article title.

## How to Use the Program
1. Download files from the repo in the directory you want to be in
    - websiteURLs.txt: contains ten URLs to different articles each in a new line
    - requirement.yaml: holds the conda environment requirements to run this prgram
    - run.py: main function that runs the program
    - Data: holds the raw html articles and the processed articles 
    - module_1: holds the scraper.py file, which is what extracts the content of the articles
    - module_2: holds the file_manager.py file, which is what saves the articles into the Data folder
    - module_3: holds the AI_summarizer.py, which implements the ai
2. Copy the conda environment 
    - type "conda env create -f requirement.yaml" into the command line
        - This will create a new environment and install all the dependencies needed to run the code from the .yaml file, and the clean up the cache
    - Double check that the environment includes 'requests', 'seautifulsoup4', 'html2text', and 'google.generativeai' by typing the command "conda list"
3. Activate the environment
4. If in Visual Studio Code, press the play button while in run.py
5. If in the terminal, type "python3 articleScraper.py"
6. Watch the processed and raw folders in the Data folder fill with the articles

## Using the API
- To use the API, you first need to obtain an API key.
    - You can do this by signing up for an account on The Gemini API website (ai.google.dev)
    - generating an API key by clicking the "Get API Key" button. 
    - Copy the given key
-  Paste the key to line 35 in run.py (api_key = 'AIzaSyDjYqjoFTUAH9uGznSeWWU-DAP0Wu5qeDI' #load your own API key)
    - This will configure Gemini to your own API. 

