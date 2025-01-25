from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")


driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()

time.sleep(2)

driver.find_element(By.XPATH, ".//span[text()='Булки']").click()

time.sleep(2)

assert driver.find_element(By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']").is_displayed()

driver.quit()