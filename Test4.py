import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://helion.pl")

szukaj = driver.find_element(By.ID,'inputSearch').send_keys('Python' + Keys.ENTER)

#webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
#wciska kontrol i nie puszczając go wcisnie litere a = zaznaczenie wszystkiego na stronie

action = webdriver.ActionChains(driver)

action.key_down(Keys.SHIFT).send_keys("a").perform()

