from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://url.do.site/login")

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.NAME, "login"))
)

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

input_element = driver.find_element(By.NAME, "login")
input_element.clear
input_element.send_keys("user_name")

input_element = driver.find_element(By.NAME, "password")
input_element.clear
input_element.send_keys("user_password" + Keys.ENTER)

time.sleep(7)

driver.quit()