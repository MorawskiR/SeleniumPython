from element import BasePageElement
from locators import MainPageLocators


class SearchTextElement(BasePageElement):
    locator = 'q'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPAge(BasePage):
    def is_title_matches(self):
        return "Python" in self.driver.title  # czy slowo puython jest w tytule

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultPage(BasePage):
    def is_result_found(self):
        return "Nie znaleziono" not in self.driver.page_source
