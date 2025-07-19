from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure


class BasePageLocators:
    LOGO_BUTTON = (By.XPATH, '//*[@class="toolbar_logo_img"]')
    VK_ECOSYSTEM_BUTTON = (By.XPATH, '//*[@class="toolbar_nav_i_ic"]')
    MORE_BUTTON = (By.XPATH, '//*[@data-l="t,more"]')
    COOKIE_BUTTON = (By.XPATH, '//button[@class="button-pro __solid-white cb_accept js-cb_accept"]')


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
            self.find_element(BasePageLocators.LOGO_BUTTON)
            self.find_element(BasePageLocators.VK_ECOSYSTEM_BUTTON)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator),
                                                      message=f"Не удалось найти элемент {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator),
                                                      message=f"Не удалось найти элементы {locator}")

    @allure.step('Открываем страницу')
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="скриншот", attachment_type=allure.attachment_type.PNG)

    @allure.step('Нажимаем на кнопку экосистемы')
    def click_vk_ecosystem(self):
        self.find_element(BasePageLocators.VK_ECOSYSTEM_BUTTON).click()

    @allure.step('Нажимаем на кнопку еще')
    def click_more_button(self):
        self.find_element(BasePageLocators.MORE_BUTTON).click()

    @allure.step('Закрываем баннер cookie')
    def close_cookie_banner(self):
        try:
            self.find_element(BasePageLocators.COOKIE_BUTTON).click()
        except TimeoutException:
            print("Баннер cookie не найден или уже закрыт.")
        except Exception as e:
            print(f"Произошла ошибка при закрытии баннера cookie: {e}")

    @allure.step('Получаем id окна браузера по индексу')
    def get_window_id(self, index):
        return self.driver.window_handles[index]

    @allure.step('Переключаемся на окно браузера')
    def switch_to_window(self, window_id):
        self.driver.switch_to.window(window_id)
