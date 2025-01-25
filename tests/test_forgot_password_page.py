from pages.forgot_password_page import ForgotPasswordPage
import allure


class TestForgotPasswordPage:

    @allure.title('Проверка открытия главной страницы')
    def test_open_main_page_from_header(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.send_password_restore_request()
        forgot_password_page.check_password_restore_request_sent()

    @allure.title('Проверка фокуса на поле пароля')
    def test_password_input_in_active_state(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.send_password_restore_request()
        forgot_password_page.click_on_focus_password_input_icon()
        forgot_password_page.check_password_input_in_active_state()
