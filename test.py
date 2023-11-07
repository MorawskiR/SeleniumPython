import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_is
driver = webdriver.Chrome()

print("Rozpoczynam test 1 ")
print("Otwieram strone")
driver.get(url='https://helion.pl')

print("strona głowna")
print("Wpisuje w wyszukiwarke")

driver.find_element(By.ID,'inputSearch').send_keys('Python' + Keys.ENTER)

print("wpisane slowo python")
print("klikam zgode")

driver.find_element(By.ID, 'rodo-ok').click()

print("Klikniecie udane")

time.sleep(2)

print("Odnajduje ksiazke o Pythonie ")


# WebDriverWait(driver,timeout=5).until(title_is('Szukasz "Python" « - Księgarnia informatyczna Helion'))
# print("czekam na tytul Python 3. Projekty dla początkujących")

WebDriverWait(driver,timeout=5).until(lambda x: x.find_element(By.CLASS_NAME, 'pytmiv--link')) #oczekiwanie jawne
print("poszukuje elementu link")
driver.find_element(By.CLASS_NAME, 'pytmiv--link').click()
print("Poszukuje elementu 'pytmie--link'")


print("odnalezione")



print("zagladam do ksiazki")
driver.find_element(By.ID,'zajrzyj').click()
time.sleep(2)
print("test 1 wykonany prawidlowo")
print("Koniec")