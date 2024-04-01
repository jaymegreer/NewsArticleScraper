# News Article Scraper
### Jayme Greer

## What the Program Does
This Python program is designed to scrap news articles and summarize them from a list of URLs provided in the text file `websiteURLs.txt`, and I chose all entertainment article types. The program uses the `requests`, `beautifulsoup4`, and `html2text` libraries to extract the main article content and save it to separate text files. It also used `google.generativeai` to summarize the articles in 50 words or under using Google's AI, Gemini. Comments in the code is added to describe as much as possible.
- It does all this by 
    - visiting each URL from the provided text file
    - saving the raw html files into the raw data folder 
    - extracting the main article content and title from the div with the class `article-body__content` and `article-hero-headline__htag`, respectively
    - converting the HTML content from the page to regular text
    - summarizing the article given the prompt and extracted article content using ai
    - saving each of the article's titles, summaries, and extracted data to individual text files named based on their article title.

## How to Use the Program
1. **Clone the Respository**
    - you should have:
        - websiteURLs.txt: contains ten URLs to different articles each in a new line
        - requirement.yaml: holds the conda environment requirements to run this prgram
        - run.py: main function that runs the program
        - Data: holds the raw html articles and the processed articles 
        - module_1: holds the scraper.py file, which is what extracts the content of the articles
        - module_2: holds the file_manager.py file, which is what saves the articles into the Data folder
        - module_3: holds the AI_summarizer.py, which implements the ai
    - make sure you are working in the correct directory
2. **Copy the Conda Environment**
    - make sure you have Python 3 installed on your system
    - to create a copy of the environment needed type the following code into your command line
    ```
    conda env create -f requirement.yaml
    ```
    ```
    conda clean -p
    ```
        - This will create a new environment and install all the dependencies needed to run the code and then clean up the cache
    - Double check that the environment includes `requests`, `beautifulsoup4`, `html2text`, and `google.generativeai` by typing the command ```
    conda list
    ```
3. **Activate the environment**
4. If in **Visual Studio Code**, press the play button while in `run.py`
5. If in the **terminal**, type 
    ```
    python3 articleScraper.py
    ```
    
6. **Check the Output** 
    - Watch the processed and raw folders in the Data folder fill with the articles
        - Each text file should contain the title of the article, the summary of the artcile in 50 words or less, and the full article text

## Using the API
1. **Obtain the API Key**
    - Sign uo for an account on the [Gemini API](https://ai.google.dev) website 
    - Click "Get API Key" to generate the key
    - Copy the given key
2. **Add the Key to the Code**
    - Paste the key to line 35 in `run.py` where it says `#load your own API key`
        - This will configure Gemini to your own API
3. **Run the Code as Stated Previously**

## Notes
**Changing URLs in `websiteURLs.txt`**
- Copy and paste the entire URL in the text file with only one URL per line
- Make sure the URLs are valid and accessible
- Gemini has safety features and may be bounded by the article content. If the article is too violent, inapropriate, etc., that article will not work and a bound error will occur. 