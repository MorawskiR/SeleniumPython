#technika oparta na klasie

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_1:
    def test(self):
        driver = webdriver.Chrome()
        self.latitude = 42.1408845
        self.longitude = -72.5033907
        self.accuracy = 100

        driver.maximize_window()