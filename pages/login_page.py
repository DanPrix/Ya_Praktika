from selenium.webdriver.common.by import By
import allure
from urls.urls import FORGOT_PASSWORD_URL
from pages.base_page import BasePage


class LoginPage(BasePage):

    forgot_password_page_link = [By.XPATH, ".//a[@href='/forgot-password']"]

    @allure.step('Проверка открытия страницы восстановления пароля')
    def check_forgot_password_page_opens(self):
        self.wait_to_be_clickable(self.forgot_password_page_link)
        self.find_element(self.forgot_password_page_link).click()
        self.wait_for_url_change(FORGOT_PASSWORD_URL)
        assert self.driver.current_url == FORGOT_PASSWORD_URL


