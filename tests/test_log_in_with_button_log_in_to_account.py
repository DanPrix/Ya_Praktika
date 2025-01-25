from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
driver.find_element(By.XPATH, ".//input[@name='name']").send_keys("NikolayKluchnikov1000@mail.ru")
driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys("123456")
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

time.sleep(2)

assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").text == 'Оформить заказ'

driver.quit()