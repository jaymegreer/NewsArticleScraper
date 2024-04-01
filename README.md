# News Article Scraper
### Jayme Greer

## What the Program Does
This Python program is designed to scrap news articles and summarize them from a list of URLs provided in the text file `websiteURLs.txt`, and I chose all entertainment article types. The program uses the `requests`, `beautifulsoup4`, and `html2text` libraries to extract the main article content and save it to separate text files. Comments in the code is added to describe as much as possible.
- It does all this by 
    - visiting each URL from the provided text file
    - saving the raw html files into the raw data folder 
    - extracting the main article content from the div with the class `article-body__content`
    - converting the HTML content from the page to regular text
    - saving each of the extracted article's data to individual text files named article1-article5

## How to Use the Program
1. **Clone the Respository**
    - you should have:
        - websiteURLs.txt: contains ten URLs to different articles each in a new line
        - requirements.yaml: holds the conda environment requirements to run this prgram
        - articleScraper.py: the program
        - article1.txt-article5.txt: output files
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
    - Double check that the environment includes `requests`, `beautifulsoup4`, and `html2text`by typing the command 
    ```
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

## Notes
**Changing URLs in `websiteURLs.txt`**
- Copy and paste the entire URL in the text file with only one URL per line
- Make sure the URLs are valid and accessible
