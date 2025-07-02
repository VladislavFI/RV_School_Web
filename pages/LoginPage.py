from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    TAB_ENTRANCE = (By.XPATH, '//a[contains(@class, "js-login-login")]')
    TAB_QR_CODE = (By.XPATH, '//a[contains(@class, "js-login-qrCode")]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "LoginForm-module")]//button[@type="submit"]')
    QR_CODE_BUTTON = (By.XPATH, '//button[.//span[text()="Войти по QR-коду"]]')
    CAN_NOT_LOGIN_BUTTON = (By.XPATH, '//button[@aria-label = "Не получается войти?"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[.//span[text()="Зарегистрироваться"]]')
    VK_LOGIN = (By.XPATH, '//i[contains(@class, "__vk_id")]')


class LoginPageHelper(BasePage):
    pass
