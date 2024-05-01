from xml.etree import ElementTree as ET
import os 

"""
Converts a multiple text files with headers and paragraphs to an HTML file.
"""
def extract_title_and_paragraph(txt_file):
    # Read text file content
    with open(txt_file, 'r') as f:  
        content = f.readlines()

    # Extract header and paragraph
    header = content[0].strip()
    paragraph = "".join(content[1:]).strip()

    return header, paragraph

def create_html(article_title, paragraph):
    # Create root element for HTML
    root = ET.Element("html")

    # Create head and body elements
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "My News Aggregation Site"
    body = ET.SubElement(root, "body")

    # Create header and paragraph elements in body
    h1 = ET.SubElement(body, "h1")
    h1.text = article_title
    p = ET.SubElement(body, "p")
    p.text = paragraph

    # Convert HTML tree to string
    html_string = ET.tostring(root, encoding="utf-8", method="html")

    return html_string

#define the name of the HTML file, path to the folder containing the text files, and the path to put place the html file
html_file = "all_news_articles.html"
folder_path = "webpage_creation/summarized"
html_path = os.path.join("webpage_creation", html_file)
#list all files in the specified folder
file_names = os.listdir(folder_path)
txt_files = [file for file in file_names if file.endswith(".txt")] #makes sure only using the txt files

with open(html_path, 'wb') as f:
  for i, txt_file in enumerate(txt_files, start=1):
    title, paragraph = extract_title_and_paragraph(os.path.join(folder_path, txt_file)) #extract the title and paragraph from the current text file
    html_content = create_html(title, paragraph) #generate the HTML content for the article
    f.write(html_content) #write the HTML content to the HTML file
    print(f"Converted text file '{txt_file}' to HTML file '{html_file}'.")

