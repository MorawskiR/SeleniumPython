from selenium import webdriver

driver = webdriver.Chrome()

#driver.get("https://helion.pl")
driver.get(url='https://helion.pl')


#aktualny stan cookies
print(driver.get_cookies())
#pobranie cookies