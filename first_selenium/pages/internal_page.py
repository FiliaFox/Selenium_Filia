from selenium.webdriver.common.by import By
from first_selenium.pages.page import Page


class InternalPage(Page):

    @property
    def log_out_button(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?logout']")

    @property
    def user_management_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=users']")

    @property
    def user_profile_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=profile']")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.ID, "loginform"))
