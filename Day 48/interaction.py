from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(article_count.text)
# article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()
search_icon = driver.find_element(By.XPATH, '//*[@id="p-search"]/a/span[1]')
search_icon.click()
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()