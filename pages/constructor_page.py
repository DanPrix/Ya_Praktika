from selenium.webdriver.common.by import By
import allure
from urls.urls import BASE_URL
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    constructor_link = (By.XPATH, ".//p[text()='Конструктор']//parent::a[@href='/']")
    ingredient_link = (By.XPATH, ".//a[starts-with(@href,'/ingredient')]")
    ingredient_counter = (By.XPATH, ".//p[starts-with(@class,'counter_counter__num')]")
    close_ingredient_modal = (By.XPATH, ".//h2[text()='Детали ингредиента']/parent::div/following-sibling::button")
    basket_element = (By.XPATH, ".//ul[starts-with(@class,'BurgerConstructor_basket')]")
    create_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    order_id_header = (By.XPATH, ".//h2[starts-with(@class, 'Modal_modal__title')]")

    @allure.step('Открытие страницы конструктора')
    def click_to_open_constructor_page(self):
        self.wait_to_be_clickable(self.constructor_link)
        self.find_element(self.constructor_link).click()
        self.wait_for_url_change(BASE_URL)

    @allure.step('Проверка открытия страницы конструктора')
    def check_constructor_page_opens(self):
        assert self.driver.current_url == BASE_URL

    @allure.step('Открытие попапа ингредиента')
    def click_to_open_ingredient_popup(self):
        self.wait_to_be_clickable(self.ingredient_link)
        self.find_element_by_index(self.ingredient_link, 0).click()
        self.wait_for_visibility(self.close_ingredient_modal)

    @allure.step('Проверка открытия попапа ингредиента')
    def check_ingredient_popup_open(self):
        assert self.find_element(self.close_ingredient_modal).is_displayed()

    @allure.step('Закрытие попапа ингредиента')
    def click_to_close_ingredient_popup(self):
        self.wait_to_be_clickable(self.close_ingredient_modal)
        self.find_element(self.close_ingredient_modal).click()
        self.wait_for_invisibility(self.close_ingredient_modal)

    @allure.step('Проверка закрытия попапа ингредиента')
    def check_ingredient_popup_close(self):
        assert self.find_element(self.close_ingredient_modal).is_displayed() is False

    @allure.step('Выбор ингредиента')
    def move_ingredient_to_basket(self):
        self.wait_to_be_clickable(self.ingredient_link)
        ingredient = self.find_element_by_index(self.ingredient_link, 0)
        basket = self.find_element(self.basket_element)
        self.drag_and_drop(ingredient, basket)

    @allure.step('Проерка выбора ингредиента')
    def check_ingredient_counter_increases(self):
        counter = self.find_element_by_index(self.ingredient_counter, 0)
        assert int(counter.text) > 0

    @allure.step('Оформить заказ')
    def create_order(self):
        self.wait_to_be_clickable(self.create_order_button)
        self.find_element(self.create_order_button).click()

    @allure.step('Проерка оформления заказа')
    def check_create_order(self):
        self.wait_for_visibility(self.order_id_header)
        order_id = self.find_element(self.order_id_header)
        assert int(order_id.text) > 0



