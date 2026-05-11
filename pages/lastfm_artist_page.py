from pages.base_page import BasePage;
from selenium.webdriver.common.by import By;
    
class LastfmArtistPage(BasePage):
    LASTEST_RELEASE_DATE = (By.CLASS_NAME, "artist-header-featured-items-item-date");
    def get_latest_release_date(self):
        return self.find_element(self.LASTEST_RELEASE_DATE).text;