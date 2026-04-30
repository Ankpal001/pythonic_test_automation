import pytest
from DriverFactory import BroswerFactory as bf
import allure
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture
def browser_initialization(request):
    driver = bf.DriverFactory.browser_init()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only act after test call (not setup/teardown)
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if isinstance(driver, WebDriver):
            # Attach screenshot to Allure
            allure.attach(

                driver.get_screenshot_as_png(),
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG
            )
