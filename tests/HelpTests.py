from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertismentCabinetHelp import AdvertisementCabinetHelpHelper

import allure

BASE_URL = 'https://ok.ru/help'


def test_help_test(browser):
    with allure.step("Открываем страницу помощи"):
        BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    with allure.step("Скроллим до раздела 'Кабинет рекламы'"):
        HelpPage.scrollToItem(HelpPageLocators.ADVERTISEMENT_CABINET)
    with allure.step("Открываем помощник по кабинету рекламы"):
        AdvertisementCabinetHelpHelper(browser)
