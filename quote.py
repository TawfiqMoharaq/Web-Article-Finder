#https://www.goodreads.com/quotes
#pip install requests
#pip install bs4
#pip install lxml

import requests
import bs4
import random

while True:
    quote_type = input("What type of quote you want? (science, life, love): ")

    if quote_type == "science" or quote_type == "life" or quote_type == "love":
        html = requests.get("https://www.goodreads.com/quotes/tag/" + quote_type)
        break
    else:
        print("Please choose one of the three options (science, life, love)")

html = html.text
html_parser = bs4.BeautifulSoup(html, "lxml")
all_quotes = html_parser.findAll("div", attrs={"class": "quoteText"})
random_number = random.randint(1, 30)
print(all_quotes[random_number].text)
