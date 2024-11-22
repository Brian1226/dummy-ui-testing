from pages.home_page import HomePage
from pages.shipping_page import ShippingPage
from utils.helper_functions import generate_random_registration_info, generate_random_shipping_info


class TestCompleteUserJourney:
    def test_complete_user_journey(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        registration_page = home_page.click_create_account()
        account_page = registration_page.register_user(**generate_random_registration_info())
        men_products_page = account_page.click_men_products()
        men_jackets_page = men_products_page.click_men_jackets()
        men_jackets_page.buy_jacket()
        men_jackets_page.show_cart()
        shipping_page = men_jackets_page.checkout()
        shipping_page.enter_shipping_details(**generate_random_shipping_info())
        shipping_page.select_shipping_method(ShippingPage.FIXED_RATE_SHIPPING)
        payment_page = shipping_page.click_next_button()
        confirmation_page = payment_page.place_order()
        confirmation_page.continue_shopping()

