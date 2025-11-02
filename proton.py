from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.secrets import get_secrets

data = get_secrets()
PASSWORD = data.get("password")
PROTONMAIL = data.get("protonmail")


USERNAME_INPUT = '//*[@id="username"]'
PASSWORD_INPUT = '//*[@id="password"]'
SUBMIT_BUTTON = '/html/body/div[1]/div[4]/div[1]/main/div[1]/div[2]/form/button'

driver = webdriver.Firefox()
driver.get("https://account.proton.me/mail")

driver.implicitly_wait(0.5)

username_box = driver.find_element(by=By.XPATH, value=USERNAME_INPUT)
password_box = driver.find_element(by=By.XPATH, value=PASSWORD_INPUT)
submit_button = driver.find_element(by=By.XPATH, value=SUBMIT_BUTTON)

username_box.send_keys(PROTONMAIL)
password_box.send_keys(PASSWORD)

submit_button.click()