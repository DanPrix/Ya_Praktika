from selenium.webdriver.common.by import By


class OrderPageLocators:
    STATION_INPUT_LOCATOR = By.XPATH, './/input[@placeholder ="* Станция метро"]'
    STATION_LOCATOR = By.XPATH, '//div[text()="Черкизовская" ]/parent::button'
    NAME_INPUT_LOCATOR = By.XPATH, './/input[@placeholder ="* Имя"]'
    LAST_NAME_INPUT_LOCATOR = By.XPATH, './/input[@placeholder ="* Фамилия"]'
    ADRESS_INPUT_LOCATOR = By.XPATH, './/input[@placeholder ="* Адрес: куда привезти заказ"]'
    PHONE_INPUT_LOCATOR = By.XPATH, './/input[@placeholder ="* Телефон: на него позвонит курьер"]'
    NEXT_PAGE_BUTTON_LOCATOR = By.XPATH, './/button[contains(text(),"Далее")]'
    DELIVERY_DAY_INPUT_LOCATOR = By.XPATH, './/input[@placeholder ="* Когда привезти самокат"]'
    DURATION_CHOICE_LOCATOR = By.XPATH, './/span[@class="Dropdown-arrow"]'
    ONE_DAY_LOCATOR = By.XPATH, './/div[contains(text(),"сутки")]'
    COLOR_CHECKBOX_LOCATOR = By.ID, 'black'
    ORDER_BUTTON_LOCATOR = By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    CONFIRMATION_BUTTON_LOCATOR = By.XPATH, './/button[contains(text(),"Да")]'
    ORDER_CONFIRMATION_TEXT_LOCATOR = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'
    ORDER_PAGE_HEADER_LOCATOR = By.CLASS_NAME, 'Order_Header__BZXOb'

