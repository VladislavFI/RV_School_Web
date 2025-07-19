from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelperHelper

import allure

BASE_URL = 'https://ok.ru/'


@allure.suite('Проверка регистрации')
@allure.title('Проверка выбора случайной страны')
def test_registration_random_country(browser):
    with allure.step('Открываем главную страницу'):
        BasePageHelper(browser).get_url(BASE_URL)
    with allure.step('Переходим на страницу регистрации'):
        LoginPage = LoginPageHelper(browser)
        LoginPage.click_registration()
    with allure.step('Выбираем случайную страну'):
        RegistrationPage = RegistrationPageHelperHelper(browser)
        Selected_country_code = RegistrationPage.select_random_country()
    with allure.step('Проверяем код выбранной страны'):
        Actual_country_code = RegistrationPage.get_phone_field_value()
        assert Selected_country_code == Actual_country_code
