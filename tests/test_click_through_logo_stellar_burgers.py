from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.XPATH, ".//a[@href='/register']").click()
driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Nikolay")
driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("NikolayKluchnikov1002@mail.ru")
driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys("123456")
driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

time.sleep(1)

driver.find_element(By.XPATH, ".//input[@name='name']").send_keys("NikolayKluchnikov1002@mail.ru")
driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys("123456")
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()

time.sleep(1)

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

driver.quit()