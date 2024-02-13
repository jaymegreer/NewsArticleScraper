Project 1 -
Jayme Greer

What this program does:
This Python program is designed to scrap news articles from a list of URLs provided in the text file 'websiteURLs.txt', and I chose all entertainment article types. The program uses the 'requests', 'beautifulsoup4', and 'html2text' libraries to extract the main article content and save it to separate text files.
It does all this by visiting each URL from the provided text file, then from there, it extracts the main article content from the div with the class='article-body__content'. Once that is all retrieved, it converts the HTML content from the page to regular text and saves each of the extracted article's data to individual text files named article1-article5. I also included comments in the code to describe as much as possible.

How to use this program:
Once files are downloaded from the repo, there should be a file called 'websiteURLs.txt', which contains five URLs to different articles each in a new line, the 'articleScraper.py' file, the output files, and the 'requirements.yaml' file. Using 'requirements.yaml', you must create a conda envirnment based off the one I used. To do that, type: " conda env create -f requirements.yaml ".
This will create a new environment and install all the dependencies needed to run the code from the .yaml file, and the clean up the cache. Double check that the environment includes 'requests', 'seautifulsoup4', and 'html2text' by typing the command "conda list". Once the environemt is created and has everything you need, make sure to activiate it, and that you are in the correct directory, which should contain all of the files that are included in the repo. From there, if you're are working in Visual Studio Code, just press the run button, but if you're using the terminal, typing "python3 articleScraper.py" will also run the program. The program will then create individual text files named article1.txt, article2.txt, etc., and each file should have the text content from the articles.

