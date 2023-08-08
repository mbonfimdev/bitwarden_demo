import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ta_bitwarden_cli import ta_bitwarden_cli as ta

bitwarden_credentials = {
    "password": config.bw_pw,
    "client_id": config.bw_clientID,
    "client_secret": config.bw_secret
}

creds = {"minha_credencial":"test_login"}

bw = ta.Bitwarden(bitwarden_credentials)

# Set up Chrome WebDriver
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 60)

    # Login no Practice Test Automation
browser.get("https://practicetestautomation.com/practice-test-login/")
wait.until(ec.presence_of_element_located((By.ID, "username")))

username_field = browser.find_element(By.ID, "username")
print("Buscando login...")
username_field.send_keys(bw.get_credentials(creds)["minha_credencial"]["login"])

password_field = browser.find_element(By.ID, "password")
print("Buscando senha...")
password_field.send_keys(bw.get_credentials(creds)["minha_credencial"]["password"])

submit_button = browser.find_element(By.ID, "submit")
submit_button.click()

wait.until(ec.presence_of_element_located((By.XPATH, "//*[text() = 'Logged In Successfully']")))
print("Logged In Successfully")
