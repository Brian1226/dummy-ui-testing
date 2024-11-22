from pages.base_page import BasePage
from pages.registration_page import RegistrationPage
from pages.account_page import AccountPage
from selenium.webdriver.common.by import By
from utils.logger import Logger
import logging
from config.urls import HOME_URL


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger().logger(logging.INFO)

    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[normalize-space()='Create an Account'][1]")
    SIGN_IN_LINK = (By.XPATH, "//a[contains(text(), 'Sign In')][1]")
    WELCOME_MESSAGE = (By.XPATH, "//div[@class='panel header']//span[@class='logged-in'][starts-with(text(), 'Welcome')]")
    USER_MENU_BUTTON = (By.XPATH, "//div[@class='panel header']//button[@type='button']")
    MY_ACCOUNT_LINK = (By.XPATH, "//div[@aria-hidden='false']//a[normalize-space()='My Account']")

    def open(self):
        super().open(HOME_URL)
        self.logger.info("Opened home page")

    def click_create_account(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_LINK).click()
        self.logger.info("Clicked on 'Create an Account' link")
        return RegistrationPage(self.driver)

    def click_sign_in(self):
        self.driver.find_element(*self.SIGN_IN_LINK).click()
        self.logger.info("Clicked on 'Sign In' link")

    def get_welcome_message(self):
        self.wait_for_visibility_of_element(*self.WELCOME_MESSAGE)
        welcome_message = self.driver.find_element(*self.WELCOME_MESSAGE).text  
        if "Welcome," in welcome_message:
            self.logger.info(f"Get welcome message: {welcome_message}")
            return True
        return False
