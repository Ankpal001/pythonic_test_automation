from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
class DriverFactory:

    @staticmethod
    def browser_init():
        options = Options()
        options.add_argument("--maximize")
        options.add_argument("--incognito")
        options.add_argument("--headless = new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        driver_path = ChromeDriverManager().install()

        # 🔥 FIX: ensure correct executable (not THIRD_PARTY file)
        options.binary_location = "/usr/bin/chromium"

        driver = webdriver.Chrome(options=options)
        return driver