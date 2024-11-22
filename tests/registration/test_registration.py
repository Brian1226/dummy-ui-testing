from pages.registration_page import RegistrationPage
from utils.helper_functions import read_test_data, generate_random_registration_info


class TestRegistration:
    def test_register_new_email(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open()
        account_page = registration_page.register_user(**generate_random_registration_info())
        assert account_page.get_registration_success_message()

    def test_register_existing_email(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open()
        registration_data = read_test_data("utils/test_data/registration.json", "register_existing_email")
        account_page = registration_page.register_user(**registration_data)
        assert not account_page.get_registration_success_message()
