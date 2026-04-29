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
        driver_path = ChromeDriverManager().install()

        # 🔥 FIX: ensure correct executable (not THIRD_PARTY file)
        if "THIRD_PARTY" in driver_path:
            driver_path = driver_path.replace("THIRD_PARTY_NOTICES.chromedriver", "chromedriver")

        service = Service(driver_path)

        driver = webdriver.Chrome(service=service, options=options)
        return driver