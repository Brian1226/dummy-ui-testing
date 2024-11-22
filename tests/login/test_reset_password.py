from pages.reset_password_page import ResetPasswordPage
from utils.helper_functions import read_test_data


class TestResetPassword:
    def test_reset_password_with_email(self, driver):
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.open()
        email = read_test_data("utils/test_data/reset_password.json", "email")
        login_page = reset_password_page.reset_password(email)
        assert login_page.get_reset_password_success_message()

    def test_reset_password_without_email(self, driver):
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.open()
        reset_password_page.reset_password("")
        assert reset_password_page.get_required_field_message()