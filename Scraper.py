"""
Web Scraper for Reddit
Author: Niklaas Cotta
"""

from bs4 import BeautifulSoup
import requests
# 502 error, need an API for reddit?

url = 'https://www.reddit.com/r/whatsthisplant/'
status = requests.get(url)
print(status)  # Status code 200 = good!

html_text = requests.get('https://www.reddit.com/r/whatsthisplant/').text
soup = BeautifulSoup(html_text, 'lxml')  # parser

posts = soup.find_all('div', class_='rpBJOHq2PR60pnwJlUyP0')
print(posts)


"""""
with open('test.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    tags = soup.find_all('tr')
    for tag in tags:
        tag_td = tag.td
        if tag.a is not None:
            tag_a = tag.a.split()[-1]
            print(tag_a)

        print(tag_td)
"""""
