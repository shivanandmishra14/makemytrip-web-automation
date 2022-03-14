import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# sys.path.insert(0, '../utility')
from utility.test_driver import test_driver_data
from locators.flight_locators import *


flight_wait, driver = test_driver_data()

driver.maximize_window()
flight_wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, login_or_create))).send_keys("Bengaluru")
time.sleep(2)
