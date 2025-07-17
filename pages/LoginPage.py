from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPageLocators:
    TAB_ENTRANCE = (By.XPATH, '//a[@data-l="t,login_tab"]')
    TAB_QR_CODE = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.XPATH, '//input[@data-l="t,login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-l="t,password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@data-l="t,sign_in"]')
    QR_CODE_BUTTON = (By.XPATH, '//a[@data-l="t,get_qr"]')
    CAN_NOT_LOGIN_BUTTON = (By.XPATH, '//a[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '(//a[@data-l="t,register"])[2]')
    VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    APPLE_BUTTON = (By.XPATH, '//*[@data-l="t,apple"]')
    ERROR_TEXT = (By.XPATH, '//div[@class="input-e login_error"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.TAB_ENTRANCE)
        self.find_element(LoginPageLocators.TAB_QR_CODE)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.QR_CODE_BUTTON)
        self.find_element(LoginPageLocators.CAN_NOT_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)
        self.find_element(LoginPageLocators.APPLE_BUTTON)

    @allure.step('Нажимаем на кнопку Login')
    def clik_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text
