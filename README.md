# Web-Article-Finder

🔹 Overview

This is a simple Python script that fetches random quotes from Goodreads
 based on the selected category.
You can choose between science, life, or love, and the program will scrape a random quote from the website.

Originally built as part of my early experiments with web scraping and Python’s BeautifulSoup library.

🔹 How It Works

The program asks the user for a category (science, life, or love).

It fetches the corresponding quotes page from Goodreads.

Using BeautifulSoup, it extracts all quote elements from the HTML.

It picks one random quote and prints it to the console.

🔹 Requirements

Install the required libraries before running the script:

pip install requests
pip install bs4
pip install lxml
