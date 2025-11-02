from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.secrets import get_secrets

data = get_secrets()
EMAIL = data.get("email")
PASSWORD = data.get("password")
PROTONMAIL = data.get("protonmail")

INPUT_BOX = '//*[@id="auth-entry-email-input"]'
CONTINUE_BUTTON = '//*[@id="main"]/div/div[1]/div[1]/div/div/button'

driver = webdriver.Firefox()

driver.get("https://jobs.northropgrumman.com/careerhub/")

driver.implicitly_wait(0.5)

input_box = driver.find_element(by=By.XPATH, value=INPUT_BOX)
submit_button = driver.find_element(by=By.XPATH, value=CONTINUE_BUTTON)

input_box.send_keys(EMAIL)
submit_button.click()

driver.quit()
