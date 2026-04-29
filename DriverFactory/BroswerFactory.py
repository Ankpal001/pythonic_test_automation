from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class DriverFactory:

    @staticmethod
    def browser_init():
        options = webdriver.ChromeOptions()
        options.add_argument("--maximize")
        options.add_argument("--incognito")
        options.add_argument("--headless = new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options = options, service = Service(ChromeDriverManager().install()))
        return driver