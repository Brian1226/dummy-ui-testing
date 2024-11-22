from pages.base_page import BasePage
from pages.home_page import HomePage
import pages.reset_password_page as rpp
from selenium.webdriver.common.by import By
from utils.logger import Logger
import logging
from config.urls import LOGIN_URL


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger().logger(logging.INFO)

    EMAIL = (By.ID, "email")
    PASSWORD = (By.NAME, "login[password]")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='send2'][1]")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
    RESET_PASSWORD_LINK = (By.XPATH, "//span[contains(text(),'Forgot Your Password?')][1]")
    RESET_PASSWORD_SUCCESS_MESSAGE = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    def open(self):
        super().open(LOGIN_URL)
        self.logger.info("Opened login page")

    def login_user(self, email, password):
        self.driver.find_element(*self.EMAIL).send_keys(email) 
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.logger.info(f"Inputted login details - Email: {email}, Password: {password}")
        self.wait_for_element_to_be_clickable(*self.LOGIN_BUTTON)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.logger.info("Submitted login form")
        return HomePage(self.driver)
    
    def get_login_error_message(self):
        self.wait_for_visibility_of_element(*self.LOGIN_ERROR_MESSAGE)
        login_error_message = self.driver.find_element(*self.LOGIN_ERROR_MESSAGE).text
        if "The account sign-in was incorrect" in login_error_message:
            self.logger.info(f"Get error message: {login_error_message}")
            return True
        return False
    
    def reset_password(self):
        self.driver.find_element(*self.RESET_PASSWORD_LINK).click()
        self.logger.info("Clicked on 'Forgot Your Password?' link")
        return rpp.ResetPasswordPage(self.driver)
    
    def get_reset_password_success_message(self):
        self.wait_for_visibility_of_element(*self.RESET_PASSWORD_SUCCESS_MESSAGE)
        reset_password_success_message = self.driver.find_element(*self.RESET_PASSWORD_SUCCESS_MESSAGE).text
        if "If there is an account" in reset_password_success_message:
            self.logger.info(f"Get reset password success message: {reset_password_success_message}")
            return True
        return False
