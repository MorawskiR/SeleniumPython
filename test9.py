from selenium import webdriver

import time

browser = webdriver.Chrome() #otwiera przegladarke Chrome
browser.get("https://www.reddit.com/") #otwiera strone reddit
browser.execute_script("window.open()") #otwiera nowa karte

print(browser.window_handles) ##podaje ID kart w odpowiedzi
#otwiercie nowej karty automatycznie robi ja aktywna

browser.switch_to.window(browser.window_handles[1]) #przelaczanie sie do nowego okna
browser.get("https://www.youtube.com")

time.sleep(3)
browser.switch_to.window(browser.window_handles[0]) #przelaczam do pierwszej karty
browser.get("https://python.org")

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)") #zjedzie do samego dolu scrollem

szerokosc = browser.get_window_size().get("width")
wysokosc = browser.get_window_size().get("height")

rozmiar = browser.get_window_size()

szer1 = rozmiar.get("width")
wys1 = rozmiar.get("height")

print(szer1, wys1) #szerokosc i wysokosc ekranu

browser.set_window_size(1024,945) #ustawianie rozdzielczosci ekranu

browser.maximize_window()#maksymalizuj - zwiekszaj na cale okno
