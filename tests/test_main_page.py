import pytest
from data import ANSWER_TEXTS
from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure
from locators.main_page_locators import MainPageLocators
from locators.header_locators import HeaderLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestMainPage:
    @allure.description('Проверяем, что при клике на вопрос ответ правильный')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, ANSWER_TEXTS[0]),
            (1, ANSWER_TEXTS[1]),
            (2, ANSWER_TEXTS[2]),
            (3, ANSWER_TEXTS[3]),
            (4, ANSWER_TEXTS[4]),
            (5, ANSWER_TEXTS[5]),
            (6, ANSWER_TEXTS[6]),
            (7, ANSWER_TEXTS[7]),
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_to_element(MainPageLocators.COOKIE_LOCATOR)
        assert main_page.get_answer_text(num) == result

    @allure.description('Проверяем, что при клике на логотип "Самоката" открывается главная страница')
    def test_scooter_logo_click(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_to_element(MainPageLocators.UPPER_ORDER_BUTTON)
        order_page.click_to_element(HeaderLocators.SCOOTER_LOGO_BUTTON)
        assert 'на пару дней' in main_page.get_text_from_element(MainPageLocators.HOME_PAGE_HEADER)

    @allure.description('Проверяем, что при клике на логотип яндекса происходит редирект и открывается главная страница'
                        ' Дзена.')
    def test_yandex_logo_click(self, driver):
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_to_element(HeaderLocators.YANDEX_LOGO_BUTTON)
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(HeaderLocators.
                                                                                         SEARCH_BUTTON_ON_DZEN_PAGE))
        assert 'Найти' in driver.find_element(*HeaderLocators.SEARCH_BUTTON_ON_DZEN_PAGE).text
