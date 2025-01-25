from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

time.sleep(2)

driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()

time.sleep(2)

assert driver.find_element(By.XPATH, ".//p[text()='Мясо бессмертных моллюсков Protostomia']").is_displayed()

driver.quit()