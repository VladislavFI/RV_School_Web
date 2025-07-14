from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.LoginPage import LoginPageLocators
import pytest

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Enter your username'
EMPTY_PASSWORD_ERROR = 'Enter password'


def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.clik_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR


def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.find_element(LoginPageLocators.LOGIN_FIELD).send_keys('testuser@gmail.com')
    LoginPage.clik_login()
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR
