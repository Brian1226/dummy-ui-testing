from pages.base_page import BasePage
import pages.home_page as hp
from selenium.webdriver.common.by import By
from utils.logger import Logger
import logging
from config.urls import CONFIRMATION_URL


class ConfirmationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger().logger(logging.INFO)

    CONTINUE_SHOPPING_BUTTON = (By.CLASS_NAME, "continue")

    def open(self):
        super().open(CONFIRMATION_URL)
        self.logger.info("Opened confirmation page")

    def continue_shopping(self):
        self.wait_for_element_to_be_clickable(*self.CONTINUE_SHOPPING_BUTTON)
        self.save_screenshot("screenshots/order_confirmation.png")
        self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()
        self.logger.info("Clicked on 'Continue Shopping' button")
        return hp.HomePage(self.driver)