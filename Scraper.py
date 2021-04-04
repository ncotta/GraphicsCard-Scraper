"""
Web Scraper for Reddit
Author: Niklaas Cotta
"""

from bs4 import BeautifulSoup


with open('test.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    tags = soup.find('span')
    print(tags)
