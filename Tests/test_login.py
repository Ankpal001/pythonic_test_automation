from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
import pytest

class TestLogin(BaseTest):
    def test_login(self):
        self.lp = LoginPage(self.driver)
        self.lp.launch_login_page()
        actual_page_title = self.lp.page_title()
        assert actual_page_title == TestData.expected_page_title