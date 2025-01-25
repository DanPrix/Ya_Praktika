from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, '//*[@id = "accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
    QUESTION_LOCATOR_8 = By.XPATH, '//*[@id="accordion__heading-7"]'
    COOKIE_LOCATOR = By.XPATH, '//*[@id="rcc-confirm-button"]'
    UPPER_ORDER_BUTTON = By.CLASS_NAME, 'Button_Button__ra12g'
    LOWER_ORDER_BUTTON = By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    QUESTIONS_HEADER_LOCATOR = By.XPATH, './/div[contains(text(),"Вопросы о важном")]'
    HOME_PAGE_HEADER = By.XPATH, './/div[@class="Home_Header__iJKdX"]'

