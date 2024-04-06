import re
import webbrowser

def detect_and_open_link(text):
    
    url_pattern = re.compile(r'https?://\S+|www\.\S+')

    
    urls = re.findall(url_pattern, text)

    if urls:
        for url in urls:
            print(f"Opening link: {url}")
            webbrowser.open(url)
    else:
        print("No links found in the text.")

def process_text_and_open_link():
    
    text_with_link = input("Enter a text containing a link: ")

    
    detect_and_open_link(text_with_link)


text_with_link = input("Enter a text containing a link: ")
detect_and_open_link(text_with_link)

process_text_and_open_link()

