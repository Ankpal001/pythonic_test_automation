import pytest
from DriverFactory import BroswerFactory as bf


@pytest.fixture
def browser_initialization(request):
    driver = bf.DriverFactory.browser_init()
    request.cls.driver = driver
    yield driver
    driver.quit()

