from pages.base_page import BasePage;
from selenium.webdriver.common.by import By;

class LastfmResultsPage(BasePage):
    def go_to_artist(self, artist_name):
        selector = f"a[title='{artist_name}']";
        ARTIST_LINK = (By.CSS_SELECTOR, selector);
        self.click(ARTIST_LINK);