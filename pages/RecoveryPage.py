from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure


class RecoveryPageLocators:
    PHONE_BUTTON = (By.XPATH, '//a[@data-l="t,phone"]')
    EMAIL_BUTTON = (By.XPATH, '//a[@data-l="t,email"]')
    QR_CODE = (By.XPATH, '//*[@class="qr_code_image"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')


class RecoveryPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем страницу восстановления'):
            self.attach_screenshot()
        self.attach_screenshot()
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
        self.find_element(RecoveryPageLocators.QR_CODE)
        self.find_element(RecoveryPageLocators.SUPPORT_BUTTON)
