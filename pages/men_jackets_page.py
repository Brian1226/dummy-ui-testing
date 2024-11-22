from pages.base_page import BasePage
from pages.shipping_page import ShippingPage
from selenium.webdriver.common.by import By
from utils.logger import Logger
import logging
from config.urls import MEN_JACKETS_URL


class MenJacketsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger().logger(logging.INFO)
        self.cart_item_count = 0

    XS_SIZE = (By.XPATH, "//div[@id='option-label-size-143-item-166'][1]")
    BLUE_COLOR = (By.XPATH, "//div[@id='option-label-color-93-item-50'][1]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//span[contains(text(),'Add to Cart')][1]")
    CART_ITEM_COUNT = (By.CLASS_NAME, "counter-number")
    SHOW_CART_LINK = (By.CLASS_NAME, "showcart")
    CHECKOUT_BUTTON = (By.ID, "top-cart-btn-checkout")

    def open(self):
        super().open(MEN_JACKETS_URL)
        self.logger.info("Opened men jackets page")

    def buy_jacket(self):
        self.wait_for_visibility_of_element(*self.XS_SIZE)
        self.scroll_to_element(self.driver.find_element(*self.XS_SIZE))
        self.driver.find_element(*self.XS_SIZE).click()
        self.driver.find_element(*self.BLUE_COLOR).click()
        self.logger.info("Selected 'XS' size and 'Blue' color for a jacket")
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
        self.logger.info("Clicked on 'Add to Cart' button")

    def wait_for_cart_item_count(self):
        return self.wait_for_text(*self.CART_ITEM_COUNT, str(self.cart_item_count + 1))

    def show_cart(self):
        self.wait_for_cart_item_count()
        self.driver.find_element(*self.SHOW_CART_LINK).click()
        self.logger.info("Clicked on cart icon to show cart")

    def checkout(self):
        self.wait_for_element_to_be_clickable(*self.CHECKOUT_BUTTON)
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        self.logger.info("Clicked on 'Proceed to Checkout' button")
        return ShippingPage(self.driver)