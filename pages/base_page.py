from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=0.1)

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_visibility_of_element(self, locator_type, locator):
        return self.wait.until(EC.visibility_of_element_located((locator_type, locator)))
    
    def wait_for_element_to_be_clickable(self, locator_type, locator):
        return self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
    
    def wait_for_text(self, locator_type, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))
    
    def save_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)