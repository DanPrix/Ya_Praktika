from selenium.webdriver.common.by import By
import allure
from urls.urls import FORGOT_PASSWORD_URL
from pages.base_page import BasePage
from faker import Faker


class ForgotPasswordPage(BasePage):

    restore_password_button = [By.XPATH, ".//button[text()='Восстановить']"]
    restore_email_input = [By.XPATH, ".//input[@name='name']"]
    restore_password_div_input = [By.XPATH, ".//input[@name='Введите новый пароль']/parent::div"]
    show_hide_password_button = [By.XPATH, ".//input[@name='Введите новый пароль']/following-sibling::div[starts-with(@class,'input__icon')]"]

    @allure.step('Отправка запроса на восстановление пароля')
    def send_password_restore_request(self):
        fake = Faker("ru_RU")
        self.wait_to_be_clickable(self.restore_password_button)
        self.find_element(self.restore_email_input).send_keys(fake.email())
        self.find_element(self.restore_password_button).click()
        self.wait_for_visibility(self.restore_password_div_input)

    @allure.step('Проверка отправки запроса на восстановление пароля')
    def check_password_restore_request_sent(self):
        self.wait_for_visibility(self.restore_password_div_input)
        assert self.find_element(self.restore_password_div_input).is_displayed()

    @allure.step('Нажатие на кнопку показать пароль')
    def click_on_focus_password_input_icon(self):
        self.wait_to_be_clickable(self.show_hide_password_button)
        self.find_element(self.show_hide_password_button).click()

    @allure.step('Проверка фокуса на поле пароля')
    def check_password_input_in_active_state(self):
        cls = self.find_element(self.restore_password_div_input).get_attribute('class')
        assert "input_status_active" in cls


