import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://helion.pl")

szukaj = driver.find_element(By.ID,'inputSearch')

#webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
#wciska kontrol i nie puszczając go wcisnie litere a = zaznaczenie wszystkiego na stronie

action = webdriver.ActionChains(driver)

action.key_down(Keys.SHIFT).send_keys_to_element(szukaj, 'python').key_up(Keys.SHIFT).send_keys('python').perform()
#wyszukuje input search i wpisuje tam python a nastepnie bez shifta


szukaj.clear()
#wyslanie do pola komende wyczyszczenia go
time.sleep(50)