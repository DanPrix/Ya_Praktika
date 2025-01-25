from pages.login_page import LoginPage
import allure


class TestOrderPage:

    @allure.title('Проверка открытия главной страницы')
    def test_open_main_page_from_header(self, driver):
        order_page = LoginPage(driver)
        order_page.open_login_page()
        order_page.check_forgot_password_page_opens()

