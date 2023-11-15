from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://helion.pl")

#driver.maximize_window()

el = driver.find_element(By.CLASS_NAME,'promotion-book')

el.screenshot('promocja1.png')
#driver.save_screenshot('zrzut3.png') #robi zrzut ekranu o nazwie ('zrzut')

