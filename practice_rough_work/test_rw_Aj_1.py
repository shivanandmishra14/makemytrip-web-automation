import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver import ActionChains

# class UtilityData:
from locators.train_locators import *


# def test_driver_data():
# global driver
# global wait
driver = webdriver.Chrome(executable_path="..//driver//chromedriver.exe")
wait = WebDriverWait(driver, 20)
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
# return wait, driver

# wait = test_driver_data()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, log_in))).click()

wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "T&Cs"))).click()

time.sleep(2)

scroll_to_top = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "APPLICABILITY")))
# scroll_to_top = driver.find_element(By.LINK_TEXT, "APPLICABILITY")

action = ActionChains(wait)

driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

driver.find_element(By.ID, "header_tab_rail").click()

# action.move_to_element(scroll_to_top).perform()

# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys("akhiljose94@gmail.com")
#
# wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button[class='capText font16'] span"))).click()
#
# time.sleep(2)
#
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("L0y@lty&H0n0r")
#
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Login']"))).click()
#
# time.sleep(2)

# wait.until(expected_conditions.visibility_of_element_located((By.ID, "fromCity"))).send_keys("Bangalore")

# time.sleep(2)

# city = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='makeFlex']")))
#
# for c in city:
#
#     if c == "BNC":
#         c.click()
#         break

#wait.until(expected_conditions.visibility_of_element_located((By.ID, from_text_field))).send_keys("SBC")

#time.sleep(2)

#wait.until(expected_conditions.visibility_of_element_located((By.ID, to_text_field))).send_keys("ERS")

time.sleep(2)

try:
    wait.until(expected_conditions.visibility_of_element_located((By.ID, from_text_field))).send_keys("SBC")
    print("YOU link found and returned")
except TimeoutException:
    print("YOU link not found ... breaking out")
    #break

try:
    wait.until(expected_conditions.visibility_of_element_located((By.ID, to_text_field))).send_keys("ERS")
    print("YOU link found and returned")
except TimeoutException:
    print("YOU link not found ... breaking out")
    #break