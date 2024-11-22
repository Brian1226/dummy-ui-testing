from pages.base_page import BasePage
from pages.men_products_page import MenProductsPage
from selenium.webdriver.common.by import By
from utils.logger import Logger
import logging
from config.urls import ACCOUNT_URL

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger().logger(logging.INFO)

    MEN_PRODUCTS_LINK = (By.XPATH, "//span[contains(text(),'Men')][1]")
    ACCOUNT_INFO_LINK = (By.XPATH, "//a[normalize-space()='Account Information']")
    REGISTRATION_SUCCESS_MESSAGE = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    def open(self):
        super().open(ACCOUNT_URL)
        self.logger.info("Opened account page")

    def click_men_products(self):
        self.scroll_to_element(self.driver.find_element(*self.MEN_PRODUCTS_LINK))
        self.driver.find_element(*self.MEN_PRODUCTS_LINK).click()
        self.logger.info("Clicked on 'Men' link")
        return MenProductsPage(self.driver)
    
    def get_registration_success_message(self):
        self.wait_for_visibility_of_element(*self.REGISTRATION_SUCCESS_MESSAGE)
        registration_success_message = self.driver.find_element(*self.REGISTRATION_SUCCESS_MESSAGE).text  
        if "Thank you for registering" in registration_success_message:
            self.logger.info(f"Get registration success message: {registration_success_message}")
            return True
        return False
