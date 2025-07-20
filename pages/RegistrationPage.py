from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure
import random


class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//div[@data-l="t,phone"]')
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//*[ @class="country-select_i"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[ @data-l="t,support"]')


class RegistrationPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.COUNTRY_LIST)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
            self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)

    def select_random_country(self):
        random_number = random.randint(0, 212)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_code = country_items[random_number].get_attribute('text')
        country_items[random_number].click()
        return country_code

    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')