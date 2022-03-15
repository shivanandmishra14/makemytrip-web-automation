import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# sys.path.insert(0, '../utility')
from utility.test_utility_driver import *
from locators.flight_locators import *

# driver = test_driver_data()

wait.until(expected_conditions.visibility_of_element_located(
    (By.CLASS_NAME, banner_close))).click()

# wait.until(expected_conditions.visibility_of_element_located(
#     (By.XPATH, login_with_google))).click()
# print(driver.current_window_handle)
# login_window = driver.window_handles[1]
# driver.switch_to.window(login_window)
# wait.until(expected_conditions.visibility_of_element_located(
#     (By.CLASS_NAME, "whsOnd zHQkBf"))).send_keys("shivanandmishra14@gmail.com")

wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, login_with_email))).click()

wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[contains(@id,'username')]"))).send_keys("shivanandmishra14@gmail.com")

