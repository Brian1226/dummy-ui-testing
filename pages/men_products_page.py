from pages.base_page import BasePage
from pages.men_jackets_page import MenJacketsPage
from selenium.webdriver.common.by import By
from utils.logger import Logger
import logging
from config.urls import MEN_PRODUCTS_URL

class MenProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger().logger(logging.INFO)

    MEN_JACKETS_LINK = (By.XPATH, "//a[contains(text(),'Jackets')]")

    def open(self):
        super().open(MEN_PRODUCTS_URL)
        self.logger.info("Opened men products page")

    def click_men_jackets(self):
        self.wait_for_visibility_of_element(*self.MEN_JACKETS_LINK)
        self.scroll_to_element(self.driver.find_element(*self.MEN_JACKETS_LINK))
        self.driver.find_element(*self.MEN_JACKETS_LINK).click()
        self.logger.info("Clicked on 'Jackets' link")
        return MenJacketsPage(self.driver)