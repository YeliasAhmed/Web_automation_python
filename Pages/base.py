import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.google.com")
e = driver.find_element(By.NAME, "q")
e.send_keys("Yelias Ahmed")
time.sleep(3)
e.send_keys(Keys.ENTER)
time.sleep(5)
