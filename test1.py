
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome(service=Service(r'chromedriver.exe'))
driver.get(url='https://helion.pl')

# driver = webdriver.Chrome()
# driver.get(url='https://helion.pl')

# driver.find_elements(By.LINK_TEXT, 'Kontakt')
driver.find_elements(By.CLASS_NAME,'title-video')