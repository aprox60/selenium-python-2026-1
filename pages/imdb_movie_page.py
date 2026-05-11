from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ImdbMoviePage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-testid='hero__primary-text']")
    RATING = (By.CSS_SELECTOR, "[data-testid='hero-rating-bar__aggregate-rating__score'] span")

    def get_title(self):
        return self.find_element(self.TITLE).text

    def get_rating(self):
        return self.find_element(self.RATING).text
