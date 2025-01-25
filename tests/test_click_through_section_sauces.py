from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()

time.sleep(2)

assert driver.find_element(By.XPATH, ".//p[text()='Соус Spicy-X']").is_displayed()

driver.quit()