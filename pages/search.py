from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# класс для взаимодействия с веб-страницей поиска на
# DuckDuckGo с использованием библиотеки Selenium.
class DuckDuckGoSearchPage:
    # Статическая переменная, содержащая URL для страницы поиска DuckDuckGo
    URL = 'https://www.duckduckgo.com'
    #кортеж с информацией о методе поиска элемента на странице по ID= "searchbox_input"
    SEARCH_INPUT = (By.ID, "searchbox_input")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
