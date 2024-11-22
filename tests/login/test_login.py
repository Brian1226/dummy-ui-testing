from pages.login_page import LoginPage
from utils.helper_functions import read_test_data


class TestLogin:
    def test_correct_email_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        correct_user_email_password = read_test_data("utils/test_data/login.json", "correct_user_email_password")
        home_page = login_page.login_user(correct_user_email_password["email"], correct_user_email_password["password"])
        assert home_page.get_welcome_message()

    def test_wrong_email_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        wrong_user_email_password = read_test_data("utils/test_data/login.json", "wrong_user_email_password")
        login_page.login_user(wrong_user_email_password["email"], wrong_user_email_password["password"])
        assert login_page.get_login_error_message()