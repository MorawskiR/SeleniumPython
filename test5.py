import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("///C:/Users/Rafal_Morawski/desktop/Videopoint/alerty.html")
# ///C:\Users\Rafal_Morawski\Desktop\Videopoint
# time.sleep(10)
driver.find_element(By.LINK_TEXT, "Kliknij, aby wyświetlić okienko alert").click()

#próba wlaczenia okienka


WebDriverWait(driver, timeout=5).until(expected_conditions.alert_is_present())
alert = driver.switch_to.alert

text = alert.text
time.sleep(5)
alert.accept()
time.sleep(5)