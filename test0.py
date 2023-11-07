# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

# Here Chrome  will be used
driver = webdriver.Chrome()

# URL of website
url = "https://helion.pl"

# Opening the website
driver.get(url)

print("strona głowna")
print("Wpisuje w wyszukiwarke")

driver.find_element(By.ID,'inputSearch').send_keys('Python' + Keys.ENTER)

print("klikam zgode")

driver.find_element(By.ID, 'rodo-ok').click()
# Getting current URL source code
get_title = driver.title

# Printing the title of this URL
print(get_title)