import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("///C:/Users/Rafal_Morawski/desktop/Videopoint/alerty.html")


driver.find_element(By.LINK_TEXT, "Kliknij, aby wyświetlić okienko prompt").click()

WebDriverWait(driver, timeout=5).until(expected_conditions.alert_is_present())

alert = Alert(driver)

alert.send_keys("Selenium!")

alert.accept()
