from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
driver =webdriver.Chrome(options=options)
driver.get("https://selenium.dev")
time.sleep(10)
driver.quit()