from pages.base_page import BasePage
import pages.login_page as lp
from selenium.webdriver.common.by import By
from config.urls import RESET_PASSWORD_URL
from utils.logger import Logger
import logging


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger().logger(logging.INFO)

    EMAIL = (By.ID, "email_address")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[contains(@class, 'submit')]")
    REQUIRED_FIELD_MESSAGE = (By.ID, "email_address-error")

    def open(self):
        self.driver.get(RESET_PASSWORD_URL)
        self.logger.info("Opened reset password page")

    def reset_password(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.logger.info(f"Inputted email to reset password - Email: {email}")
        self.wait_for_element_to_be_clickable(*self.RESET_PASSWORD_BUTTON)
        self.driver.find_element(*self.RESET_PASSWORD_BUTTON).click()
        self.logger.info("Submitted reset password form")
        return lp.LoginPage(self.driver)
    
    def get_required_field_message(self):
        self.wait_for_visibility_of_element(*self.REQUIRED_FIELD_MESSAGE)
        required_field_message = self.driver.find_element(*self.REQUIRED_FIELD_MESSAGE).text
        if "This is a required field" in required_field_message:
            self.logger.info(f"Get required field message: {required_field_message}")
            return True
        return False
