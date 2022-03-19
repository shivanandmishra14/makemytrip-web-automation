from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# sys.path.insert(0, '../utility')
from utility.test_driver import test_driver_data

wait = test_driver_data()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'react-autosuggest__input')]"))).click()



