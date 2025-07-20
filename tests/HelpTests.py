from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
from pages.AdvertismentCabinetHelp import AdvertisementCabinetHelpHelper

import allure

BASE_URL = 'https://ok.ru/help'


def test_help_test(browser):
    with allure.step("Открываем страницу помощи"):
        BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHelper(browser)
    with allure.step("Скроллим до раздела 'Кабинет рекламы'"):
        HelpPage.scrollToItem(HelpPageLocators.ADVERTISEMENT_CABINET)
    with allure.step("Открываем помощник по кабинету рекламы"):
        AdvertisementCabinetHelpHelper(browser)
