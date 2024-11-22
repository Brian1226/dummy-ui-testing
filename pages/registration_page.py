from pages.base_page import BasePage
from pages.account_page import AccountPage
from selenium.webdriver.common.by import By
from utils.logger import Logger
import logging
from config.urls import REGISTRATION_URL


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger().logger(logging.INFO)
    
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    PASSWORD_CONFIRMATION = (By.ID, "password-confirmation")
    REGISTER_BUTTON = (By.XPATH, "//button[@title='Create an Account']")

    def open(self):
        self.driver.get(REGISTRATION_URL)
        self.logger.info(f"Opened registration page")

    def register_user(self, first_name, last_name, email, password):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.PASSWORD_CONFIRMATION).send_keys(password)
        self.logger.info(f"Inputted registration details - First Name: {first_name}, Last Name: {last_name}, Email: {email}, Password: {password}")
        self.wait_for_element_to_be_clickable(*self.REGISTER_BUTTON)
        self.scroll_to_element(self.driver.find_element(*self.REGISTER_BUTTON))
        self.driver.find_element(*self.REGISTER_BUTTON).click()
        self.logger.info("Submitted registration form")
        return AccountPage(self.driver)
