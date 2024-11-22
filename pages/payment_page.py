from pages.base_page import BasePage
from pages.confirmation_page import ConfirmationPage
from selenium.webdriver.common.by import By
from utils.logger import Logger
import logging
from config.urls import PAYMENT_URL


class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger().logger(logging.INFO)

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@title='Place Order']")
    ORDER_TOTAL = (By.XPATH, "//tr[@class='grand totals']//span")

    def open(self):
        super().open(PAYMENT_URL)
        self.logger.info("Opened payment page")

    def place_order(self):
        self.wait_for_visibility_of_element(*self.ORDER_TOTAL)
        self.wait_for_element_to_be_clickable(*self.PLACE_ORDER_BUTTON)
        self.scroll_to_element(self.driver.find_element(*self.PLACE_ORDER_BUTTON))
        self.driver.find_element(*self.PLACE_ORDER_BUTTON).click()
        self.logger.info("Clicked on 'Place Order' button")
        return ConfirmationPage(self.driver)