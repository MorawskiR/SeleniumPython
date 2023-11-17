import timeit #stoper co startuje w momencie wykonania linijki kodu i konca
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#testowanie bez uruchamiania przegladarki zakonczy sie zwracajac wyniki

start = timeit.default_timer()


chrome_options = Options() #ustaweioenia przegldarki chrome
chrome_options.add_argument("--headless") #uruchom browser w trybie headless
chrome_options.add_argument("--window-size=1920x1080") #rozdzielczosc ekranu

service = Service("chromedriver.exe") #selenium pakiet 4
driver = webdriver.Chrome(options=chrome_options) #przekazanie do chroma

driver.get("https://helion.pl")

driver.maximize_window()

driver.find_element(By.ID, 'inputSearch').send_keys("Selenium")

stop = timeit.default_timer() #zatrzymanie timera
print('Czas wykonania: ', stop-start) #czas wykonania
