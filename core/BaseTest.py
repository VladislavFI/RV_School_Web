import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor="http://185.207.0.170:4444", options=options)
    yield driver
    if driver:
        driver.quit()
    driver.quit()
