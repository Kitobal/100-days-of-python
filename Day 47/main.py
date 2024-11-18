from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)
product_page = response.text
soup = BeautifulSoup(product_page, "html.parser")

price_text = soup.find(name="span", class_="aok-offscreen").getText()
price = float(price_text.split("$")[1])
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100

if price < BUY_PRICE:
    message = f"{title} is on sale for {price_text}"
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["MY_EMAIL"], os.environ["MY_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=os.environ["MY_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
