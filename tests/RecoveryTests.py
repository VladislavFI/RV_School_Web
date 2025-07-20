from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper

import allure

BASE_URL = 'https://ok.ru/'
LOGINT_TEXT = 'test@gmail.com'
PASSWORD_TEXT = '123456789'

@allure.suite('Проврка восстановления')
@allure.title('Проверка перехода к восстановлению после нескеольких неудачных попыток входа')
def test_go_to_recovery(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)

    for i in range(3):
        LoginPage.type_login(LOGINT_TEXT)
        LoginPage.type_password(PASSWORD_TEXT)
        LoginPage.clik_login()

    LoginPage.click_recovery()
    RecoveryPageHelper(browser)
