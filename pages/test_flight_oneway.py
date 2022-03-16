from constant.constant_data import *
from locators.flight_locators import *
from practice_rough_work.test_new_login import wait
from utility.test_utility_driver import *

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
        (By.XPATH, username_input))).send_keys(username)

wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, user_login_continue))).click()

wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, password_input))).send_keys(password)

wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, user_login_btn))).click()

# driver.close()


