from pages.base_page import BasePage
from pages.payment_page import PaymentPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.logger import Logger
import logging
from config.urls import SHIPPING_URL


class ShippingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger().logger(logging.INFO)

    ADDRESS = (By.NAME, "street[0]")
    CITY = (By.NAME, "city")
    STATE = (By.NAME, "region_id")
    ZIP_CODE = (By.NAME, "postcode")
    COUNTRY = (By.NAME, "country_id")
    PHONE_NUMBER = (By.NAME, "telephone")
    FIXED_RATE_SHIPPING = (By.NAME, "ko_unique_1")
    TABLE_RATE_SHIPPING = (By.NAME, "ko_unique_2")
    NEXT_BUTTON = (By.CLASS_NAME, "continue")

    def open(self):
        super().open(SHIPPING_URL)
        self.logger.info("Opened shipping page")

    def enter_shipping_details(self, address, city, state, zip_code, phone_number):
        self.wait_for_visibility_of_element(*self.ADDRESS)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.CITY).send_keys(city)
        
        state_dropdown = self.driver.find_element(*self.STATE)
        state_dropdown.click()
        select = Select(state_dropdown)
        select.select_by_visible_text(state)

        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)

        country_dropdown = self.driver.find_element(*self.COUNTRY)
        country_dropdown.click()
        select = Select(country_dropdown)
        select.select_by_visible_text("United States")

        self.driver.find_element(*self.PHONE_NUMBER).send_keys(phone_number)
        self.logger.info(f"Inputted shipping details - Address: {address}, City: {city}, State: {state}, Zip Code: {zip_code}, Country: United States, Phone Number: {phone_number}")

    def select_shipping_method(self, shipping_method):
        self.wait_for_element_to_be_clickable(*shipping_method)
        self.scroll_to_element(self.driver.find_element(*shipping_method))
        selected_shipping_method = self.driver.find_element(*shipping_method)
        selected_shipping_method.click()
        shipping_method_value = selected_shipping_method.get_attribute("value")
        self.logger.info(f"Selected shipping method: {shipping_method_value}")

    def click_next_button(self):
        self.wait_for_element_to_be_clickable(*self.NEXT_BUTTON)
        self.driver.find_element(*self.NEXT_BUTTON).click()
        self.logger.info("Clicked on 'Next' button")
        return PaymentPage(self.driver)