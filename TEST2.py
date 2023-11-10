import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com")

driver.find_element(By.ID, "L2AGLb").click()

gmail = driver.find_element(By.LINK_TEXT,"Gmail")



x = 100
y = 100


#webdriver.ActionChains(driver).move_to_element(gmail).perform()
#ma zatrzymany kursor na przycisku gmail
webdriver.ActionChains(driver).move_by_offset(x,y).perform()
#przesuwa kursor x i y o 100 px

time.sleep(50)
