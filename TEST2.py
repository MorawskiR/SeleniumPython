import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com")

driver.find_element(By.ID, "L2AGLb").click()

gmail = driver.find_element(By.LINK_TEXT,"Gmail")

webdriver.ActionChains(driver).move_to_element(gmail).perform()
#ma zatrzymany kursor na przycisku gmail

time.sleep(50)
