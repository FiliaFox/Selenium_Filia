from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException


class Page(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver,10)

    def is_element_visible(self, locator):
        try:
            return self.wait.until(visibility_of_all_elements_located(locator))
        except WebDriverException:
            return False
