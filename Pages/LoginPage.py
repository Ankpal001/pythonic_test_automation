from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
class LoginPage(BasePage):

     username = (By.XPATH,"//input[@id = 'user-name']")
     password = (By.XPATH, "//input[@id = 'password']")
     login_but = (By.XPATH, "//input[@id = 'login-button']")
     prods = (By.XPATH, "//span[text() = 'Products']")
     def __init__(self, driver):
         super().__init__(driver)
     def launch_login_page(self):
         self.launch_url(TestData.login_url)
     def do_login(self):
         self.do_send_keys(self.username,TestData.login_name)
         self.do_send_keys(self.password, TestData.login_password)
         self.do_click(self.login_but)
         return self.get_element(self.prods).text


