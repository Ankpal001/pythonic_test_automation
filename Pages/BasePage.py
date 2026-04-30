from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from Config.config import TestData


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def launch_url(self, url):
        self.driver.get(url)
    def page_title(self):
        return self.driver.title
    def get_element(self, locator):
        return self.driver.find_element(*locator)
    def do_send_keys(self, locator, value):
        self.get_element(locator).send_keys(value)
    def do_click(self, locator):
        self.get_element(locator).click()