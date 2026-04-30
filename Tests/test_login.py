from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
import pytest

class TestLogin(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login(self):
        self.lp = LoginPage(self.driver)
        self.lp.launch_login_page()
        actual_page_title = self.lp.page_title()
        assert actual_page_title == TestData.expected_page_title
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_user(self):
        self.lp = LoginPage(self.driver)
        self.lp.launch_login_page()
        home_page_prods =self.lp.do_login()
        assert home_page_prods == TestData.home_page_title