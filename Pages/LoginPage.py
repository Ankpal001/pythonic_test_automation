from Config.config import TestData
from Pages.BasePage import BasePage
class LoginPage(BasePage):

     def __init__(self, driver):
         super().__init__(driver)
     def launch_login_page(self):
         self.launch_url(TestData.login_url)


