from selenium import webdriver
class DriverFactory:

    @staticmethod
    def browser_init():
        options = webdriver.ChromeOptions()
        options.add_argument("--maximize")
        options.add_argument("--incognito")
        options.add_argument("--headless")
        driver = webdriver.Chrome(options = options)
        return driver