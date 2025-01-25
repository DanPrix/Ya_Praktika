from selenium.webdriver.common.by import By
import allure
from urls.urls import FEED_URL
from pages.base_page import BasePage


class FeedPage(BasePage):

    feed_lnk = (By.XPATH, ".//a[@href='/feed']")
    history_item = (By.XPATH, ".//li[starts-with(@class, 'OrderHistory_listItem')]")
    history_id = (By.XPATH, ".//p[starts-with(@class, 'text text_type_digits-default')]")
    item_info_header = (By.XPATH, ".//p[text()='Cостав']")
    order_counter = (By.XPATH, ".//p[starts-with(@class, 'OrderFeed_number__')]")
    not_ready_orders = (By.XPATH, ".//ul[starts-with(@class, 'OrderFeed_orderListReady__')]/li[starts-with(@class, 'text text_type_digits-default')]")

    @allure.step('Открытие страницы ленты заказа')
    def click_to_open_feed_page(self):
        self.wait_to_be_clickable(self.feed_lnk)
        self.find_element(self.feed_lnk).click()
        self.wait_for_url_change(FEED_URL)

    @allure.step('Проверка открытия страницы ленты заказов')
    def check_feed_page_opens(self):
        assert self.driver.current_url == FEED_URL

    @allure.step('Открытие информации о заказе')
    def click_to_open_order_info(self):
        self.wait_to_be_clickable(self.history_item)
        self.find_element_by_index(self.history_item, 0).click()

    @allure.step('Проверка открытия информации о заказе')
    def check_open_order_info(self):
        self.wait_for_visibility(self.item_info_header)
        assert self.find_element(self.item_info_header).is_displayed()

    @allure.step('Проверка наличия своего заказа в общем списке')
    def check_order_id_in_all_orders(self, order_id):
        self.wait_for_visibility(self.history_id)
        for item in self.find_all_elements(self.history_id):
            if item.text == order_id:
                break
        else:
            assert False
        assert True

    @allure.step('Получение счетчиков заказов')
    def get_order_counters(self):
        self.wait_for_visibility(self.order_counter)
        counters = self.find_all_elements(self.order_counter)
        return int(counters[0].text), int(counters[1].text)

    @allure.step('Получение счетчиков заказов')
    def get_not_ready_order_ids(self):
        self.wait_for_visibility(self.not_ready_orders)
        elements = self.find_all_elements(self.not_ready_orders)
        return list(map(lambda e: e.text, elements))



