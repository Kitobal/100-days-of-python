from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfEunuYkEZ5GWH3fMmYRNPWX30p7bhCt_MswPblbokfLie8cw/viewform?usp=sf_link"
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_LINK)
zillow_page = response.text
soup = BeautifulSoup(zillow_page, "html.parser")

all_links = soup.find_all(name="a", class_="property-card-link")
links = []
for link in all_links:
    links.append(link.get("href"))

all_addresses = soup.find_all(name="address")
addresses = [address.get_text().replace(" | ", " ").strip() for address in all_addresses]
# print(addresses)

all_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_prices if "$" in price.text]
# print(prices)


# selenium part

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(links)):
    driver.get(FORM_LINK)
    time.sleep(3)

    address = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(addresses[n])
    price.send_keys(prices[n])
    link.send_keys(links[n])
    time.sleep(1)
    submit_button.click()