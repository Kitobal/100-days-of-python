from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from config import MY_EMAIL,MY_PASSWORD
import time


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/")


# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

time.sleep(2)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(MY_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(MY_PASSWORD)
password_field.send_keys(Keys.ENTER)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4078852135&f_WT=2&keywords=Python%20Developer&refresh=true")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        save_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
        save_button.click()
        print("Saved")


    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue


time.sleep(5)
driver.quit()


