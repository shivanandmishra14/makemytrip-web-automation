from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# sys.path.insert(0, '../utility')
from utility.test_driver import test_driver_data

wait = test_driver_data()
wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "//span[@class='chNavIcon appendBottom2 chSprite chFlights active']"))).click()

wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "(//span[@class='lbl_input latoBold  appendBottom5'])[1]"))).click()
