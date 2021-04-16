"""
Web Scraper for Amazon
Author: Niklaas Cotta
Used this video as a tutorial: https://www.youtube.com/watch?v=Bg9r_yLk7VY
"""

from bs4 import BeautifulSoup
import requests


def pricing():
    url = 'https://www.amazon.com/dp/B08G5CQMJ3/ref=olp_aod_early_redir?_encoding=UTF8&aod=1&qid=1618611274&sr=8-3'

    # Doesn't work otherwise!!
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    print(soup.prettify())

    productName = soup.find(id="productTitle").get_text()

    try:
        price = soup.find(id="priceblock_ourprice").get_text()
    except AttributeError:
        price = ""

    return productName, price


def printPrice(product):
    (name, price) = product
    print("Name: ", name.strip()[0:64])
    print("Price: ", price.strip())

    if not price:
        # thirdParty =
        print("Product is not available for purchase by amazon at this time")
        print("Cheapest third party price: ")


if __name__ == '__main__':
    productPrice = pricing()
    printPrice(productPrice)
