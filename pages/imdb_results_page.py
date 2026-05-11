from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ImdbResultsPage(BasePage):
    FIRST_RESULT = (By.CSS_SELECTOR, ".ipc-title-link-wrapper")

    def go_to_first_result(self):
        self.click(self.FIRST_RESULT)
