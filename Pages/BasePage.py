from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def launch_url(self, url):
        self.driver.get(url)
    def page_title(self):
        return self.driver.title