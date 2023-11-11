from selenium import webdriver

driver = webdriver.Chrome()

#driver.get("https://helion.pl")
driver.get(url='https://helion.pl')

#driver.add_cookie({"name":"tomek","value":"selenium"})
#zmiana dodanie cookies
#driver.delete_all_cookies() #usuniecie wszystkich cookies

driver.delete_cookie("tomek") #podajemy wartosc nie pole

# #aktualny stan cookies
# print(driver.get_cookies())
#pobranie cookies

print(driver.get_cookie("name"))