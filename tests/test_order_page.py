import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:
    @allure.description('Проверяем, что при клике на верхнюю кнопку "заказать" открывается страница заказа')
    def test_upper_order_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_to_element(MainPageLocators.UPPER_ORDER_BUTTON)
        assert order_page.get_text_from_element(OrderPageLocators.ORDER_PAGE_HEADER_LOCATOR) == 'Для кого самокат'

    @allure.description('Проверяем, что при клике на нижнюю кнопку "заказать" открывается страница заказа')
    def test_lower_order_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_to_element(MainPageLocators.COOKIE_LOCATOR)
        main_page.scroll_to_element(MainPageLocators.QUESTIONS_HEADER_LOCATOR)
        main_page.find_element_with_wait(MainPageLocators.LOWER_ORDER_BUTTON)
        main_page.click_to_element(MainPageLocators.LOWER_ORDER_BUTTON)
        assert order_page.get_text_from_element(OrderPageLocators.ORDER_PAGE_HEADER_LOCATOR) == 'Для кого самокат'

    @allure.description('Тестируем весь флоу оформления заказа и убеждаемся что он оформлен')
    @pytest.mark.parametrize(
        'name, last_name, address, day',
        [
            ('Петя', 'Иванов', 'Москва', '11.11.2024'),
            ('Вася', 'Сидоров', 'Химки', '14.11.2024')
        ]
    )
    def test_successful_order(self, driver, name, last_name, address, day):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_to_element(MainPageLocators.COOKIE_LOCATOR)
        main_page.click_to_element(MainPageLocators.UPPER_ORDER_BUTTON)
        order_page.set_order(name, last_name, address, day)
        assert 'Заказ оформлен' in order_page.check_order()
