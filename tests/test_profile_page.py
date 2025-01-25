import time

from pages.profile_page import ProfilePage
import allure


class TestProfilePage:

    @allure.title('Проверка открытия главной страницы')
    def test_open_profile_from_header(self, driver_logged_in):
        profile_page = ProfilePage(driver_logged_in)
        profile_page.open_profile_page()
        profile_page.check_profile_page_opens()

    @allure.title('Проверка открытия главной страницы')
    def test_open_order_history_page(self, driver_logged_in):
        profile_page = ProfilePage(driver_logged_in)
        profile_page.open_profile_page()
        profile_page.open_order_history_page()
        profile_page.check_order_history_page_opens()

    @allure.title('Проверка выхода из ЛК')
    def test_logout(self, driver_logged_in):
        profile_page = ProfilePage(driver_logged_in)
        profile_page.open_profile_page()
        profile_page.logout()
        profile_page.check_logout()

