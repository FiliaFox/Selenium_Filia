class Application(object):

    def __init__(self, driver):
        self.driver = driver

    def go_to_home(self):
        self.driver.get("http://localhost:8888/php4dvd/")

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Log out").click()
        driver.switch_to_alert().accept()

    def login(self, user):
        driver = self.driver
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user.username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user.password)
        driver.find_element_by_name("submit").click()
