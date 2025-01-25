import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls.urls import REGISTER_URL, LOGIN_URL, BASE_URL
from faker import Faker

ANY_INPUT_LOCATOR = ".//main//form//input"
EMAIL_OR_NAME_LOCATOR = ".//main//form//input[@name='name']"
PASSWORD_LOCATOR = ".//main//form//input[@name='Пароль']"
REGISTER_BUTTON_LOCATOR = ".//main//form/button"
EMAIL_LOCATOR = ".//main//form//input[@name='name']"
LOGIN_BUTTON_LOCATOR = ".//button[text()='Войти']"


@pytest.fixture()
def random_email():
    return Faker().email()


@pytest.fixture()
def random_password():
    return Faker().password()


@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError()
    yield driver
    driver.quit()


@pytest.fixture()
def driver_registered(driver, random_email, random_password):
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
    for input_element in driver.find_elements(By.XPATH, EMAIL_OR_NAME_LOCATOR):
        input_element.send_keys(random_email)
    driver.find_element(By.XPATH, PASSWORD_LOCATOR).send_keys(random_password)
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, REGISTER_BUTTON_LOCATOR).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.url_to_be(LOGIN_URL))
    yield driver
    driver.quit()


@pytest.fixture()
def driver_logged_in(driver_registered, random_email, random_password):
    driver_registered.get(LOGIN_URL)
    WebDriverWait(driver_registered, 3).until(
        expected_conditions.url_to_be(LOGIN_URL))
    driver_registered.find_element(By.XPATH, EMAIL_LOCATOR).send_keys(random_email)
    driver_registered.find_element(By.XPATH, PASSWORD_LOCATOR).send_keys(random_password)
    driver_registered.find_element(By.XPATH, LOGIN_BUTTON_LOCATOR).click()
    WebDriverWait(driver_registered, 3).until(
        expected_conditions.url_to_be(BASE_URL))
    yield driver_registered
    driver_registered.quit()
