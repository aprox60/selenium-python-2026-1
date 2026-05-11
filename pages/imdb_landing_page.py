from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class ImdbLandingPage(BasePage):
    SEARCH_INPUT = (By.ID, "suggestion-search")
    SEARCH_BTN = (By.ID, "suggestion-search-button")

    def search_movie(self, movie_name):
        self.enter_text(self.SEARCH_INPUT, movie_name)
        self.find_element(self.SEARCH_INPUT).send_keys(Keys.ENTER)
