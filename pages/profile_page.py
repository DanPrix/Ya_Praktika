from selenium.webdriver.common.by import By
import allure
from urls.urls import PROFILE_URL, ORDER_HISTORY_URL, LOGIN_URL
from pages.base_page import BasePage


class ProfilePage(BasePage):

    profile_page_link = [By.XPATH, ".//a[@href='/account']"]
    order_history_link = [By.XPATH, ".//a[@href='/account/order-history']"]
    logout_button = [By.XPATH, ".//button[text()='Выход']"]
    order_id = [By.XPATH, ".//p[starts-with(@class, 'text text_type_digits-default')]"]

    @allure.step('Открытие страницы профиля')
    def open_profile_page(self):
        self.wait_to_be_clickable(self.profile_page_link)
        self.find_element(self.profile_page_link).click()
        self.wait_for_url_change(PROFILE_URL)

    @allure.step('Проверка открытия страницы профиля')
    def check_profile_page_opens(self):
        assert self.driver.current_url == PROFILE_URL

    @allure.step('Открытие страницы истории заказов')
    def open_order_history_page(self):
        self.wait_to_be_clickable(self.order_history_link)
        self.find_element(self.order_history_link).click()
        self.wait_for_url_change(ORDER_HISTORY_URL)

    @allure.step('Получение последнего id заказа')
    def get_last_order_id(self):
        self.wait_for_visibility(self.order_id)
        return self.find_element_by_index(self.order_id, 0).text

    @allure.step('Проверка открытия страницы истории заказов')
    def check_order_history_page_opens(self):
        assert self.driver.current_url == ORDER_HISTORY_URL

    @allure.step('Выход из ЛК')
    def logout(self):
        self.wait_to_be_clickable(self.logout_button)
        self.find_element(self.logout_button).click()
        self.wait_for_url_change(LOGIN_URL)

    @allure.step('Проверка выхода из ЛК')
    def check_logout(self):
        assert self.driver.current_url == LOGIN_URL



