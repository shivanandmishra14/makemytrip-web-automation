import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# class UtilityData:
driver = webdriver.Chrome(executable_path="..\\driver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
wait = WebDriverWait(driver, 20)

# Close card
wait.until(expected_conditions.visibility_of_element_located(
    (By.CLASS_NAME, "langCardClose"))).click()

wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "//span[text()='Google']"))).click()

print(driver.current_window_handle)
login_window = driver.window_handles[1]
driver.switch_to.window(login_window)

wait.until(expected_conditions.visibility_of_element_located(
    (By.CLASS_NAME, "whsOnd zHQkBf"))).send_keys("shivanandmishra14@gmail.com")
