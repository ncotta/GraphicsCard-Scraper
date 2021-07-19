"""
A multipurpose web scraper for python. Currently set for graphics cards
Author: Niklaas Cotta
Sources: https://www.youtube.com/watch?v=Bg9r_yLk7VY
         https://www.youtube.com/watch?v=5iWhQWVXosU
"""

from bs4 import BeautifulSoup
from decouple import config
import requests
import smtplib  # simple mail transfer protocol SMTP
import time

sender = config('EMAIL_USER')  # environmental variables for security, in .env
password = config('EMAIL_PASS')

url = 'https://smile.amazon.com/ZOTAC-GeForce-Graphics-IceStorm-ZT-A30600H-10M/dp/B08W8DGK3X/ref=sr_1_2?dchild=1' \
          '&keywords=3060+ti&qid=1626711515&sr=8-2'


def getPrice():
    # Doesn't work otherwise!!
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    # print(soup.prettify())

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

    else:
        if int(price) <= 800:
            sendEmail()


def sendEmail():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()  # identify self with mail server
        smtp.starttls()  # encrypt traffic
        smtp.ehlo()  # re-identify self with encrypted connection

        smtp.login(sender, password)
        (name, price) = getPrice()

        subject = "Graphics Card Price Alert!  - GraphicsBot"
        body = f"A graphics card has recently decreased in price\n" \
               f"Name: {name}" \
               f"URL: {url}\n\n" \
               f"New price: {price}" \
               f"This is an automated message. :)"
        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(sender, "nikcotta@gmail.com", msg)

        smtp.quit()


if __name__ == '__main__':
    while True:
        productPrice = getPrice()
        printPrice(productPrice)
        time.sleep(86400)  # check once a day
