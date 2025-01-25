from pages.base_page import BasePage
from locators.main_page_locators import (MainPageLocators)
import allure


class MainPage(BasePage):

    @allure.step('Получаем текст с ответа')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_8)
        self.find_element_with_wait(locator_q_formatted)
        self.click_to_element(locator_q_formatted)
        self.find_element_with_wait(locator_a_formatted)
        return self.get_text_from_element(locator_a_formatted)



