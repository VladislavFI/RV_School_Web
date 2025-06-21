import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(self):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
