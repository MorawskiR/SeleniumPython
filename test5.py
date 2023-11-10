from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("///C:\Users\Rafal_Morawski\Desktop\Videopoint")

driver.find_element(By.LINK_TEXT, "Kliknij, aby wyświetlić okienko alert").click()
#próba wlaczenia okienka


alert = WebDriverWait(driver,timeout = 5).until(expected_conditions.alert_is_presented())
text = alert.text

alert.accept()