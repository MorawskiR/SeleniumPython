import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

import page


#podejscie obiektowe
#OCP - open case principle
#SOLID  klasa ktora mozna rozszerzac
class PythonorgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.python.org") #setup otwarcia przegladarki i strony
      #  self.assertEquals(True,False) #add assertion here
    def test_search_in_python_org(self, search_results_page=None): #opis co bedzie robi
        main_page=page.MainPAge(self.driver) # strona glowna,
        main_page.search_text_element = "pycon" # szuka / wpisuje text
        main_page.click_go_button() #wywoluje button
        search_result_page = page.SearchResultPage(self.driver)
        assert search_results_page.is_result_founf(),"Nie znaleziono."

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()