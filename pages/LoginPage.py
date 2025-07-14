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
    OTHER_BUTTON = (By.XPATH, '//*[@data-l="t,other"]')
    ERROR_TEXT = (By.XPATH, '//div[@class="input-e login_error"]')
    BUTTON_RESTORE = (By.XPATH, '//button[@data-l="t,restore"]')
    BUTTON_BACK = (By.XPATH, '//button[@data-l="t,cancel"]')
    BUTTON_SUPPORT = (By.XPATH, '(//*[@class="external-oauth-login_title-tx"])[2]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        # self.check_page()

    def check_page(self):
        with allure.step('Проверяем страницу восстановления'):
            self.attach_screenshot()
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
        self.find_element(LoginPageLocators.OTHER_BUTTON)

    @allure.step('Нажимаем на кнопку Login')
    def clik_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Вводим логин')
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Вводим пароль')
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Нажимаем на кнопку восстановления')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.BUTTON_RESTORE).click()