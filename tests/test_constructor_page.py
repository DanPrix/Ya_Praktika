from pages.constructor_page import ConstructorPage
import allure


class TestConstructorPage:

    @allure.title('Проверка открытия страницы конструктора')
    def test_open_profile_from_header(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_login_page()
        constructor_page.click_to_open_constructor_page()
        constructor_page.check_constructor_page_opens()

    @allure.title('Проверка открытия попапа ингредиента')
    def test_open_profile_from_header(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()
        constructor_page.click_to_open_ingredient_popup()
        constructor_page.check_ingredient_popup_open()

    @allure.title('Проверка закрытия попапа ингредиента')
    def test_open_profile_from_header(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()
        constructor_page.click_to_open_ingredient_popup()
        constructor_page.click_to_close_ingredient_popup()
        constructor_page.check_ingredient_popup_close()

    @allure.title('Проверка увеличения счетчика ингредиента')
    def test_increment_ingredient_counter(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()
        constructor_page.move_ingredient_to_basket()
        constructor_page.check_ingredient_counter_increases()

    @allure.title('Проверка создания заказа для залогиненного пользователя')
    def test_increment_ingredient_counter(self, driver_logged_in):
        constructor_page = ConstructorPage(driver_logged_in)
        constructor_page.open_main_page()
        constructor_page.move_ingredient_to_basket()
        constructor_page.create_order()
        constructor_page.check_create_order()


