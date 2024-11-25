from config import USERNAME,PASSWORD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

SIMILAR_ACCOUNT = "elderscrollsonline"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4.2)
        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")
        username.send_keys(USERNAME)
        time.sleep(2)
        password.send_keys(PASSWORD)
        time.sleep(2.1)
        password.send_keys(Keys.ENTER)
        time.sleep(4.3)

    def find_followers(self):
        time.sleep(5)
        self.driver.get("https://www.instagram.com/elderscrollsonline")
        time.sleep(4)
        follower = self.driver.find_element(By.CSS_SELECTOR, f'a[href="/elderscrollsonline/followers/"]')
        follower.click()
        time.sleep(5.2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Follow')]")
        for element in follow_buttons:
            try:
                element.click()
            except NoSuchElementException:
                pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
