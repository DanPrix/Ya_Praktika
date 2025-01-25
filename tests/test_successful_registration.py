from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.XPATH, ".//a[@href='/register']").click()
driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Nikolay")
driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("NikolayKluchnikov1000@mail.ru")
driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys("123456")
driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

time.sleep(1)

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()