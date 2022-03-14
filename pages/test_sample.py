# import pytest
# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support import expected_conditions as EC
#
# # sys.path.insert(0, '../utility')
# from utility.test_driver import test_driver_data
# from locators.flight_locators import *
#
# # class UtilityData:
# global driver
# global wait
#
#
# def test_driver_data_1():
#     global driver
#     global wait
#     driver = webdriver.Chrome(executable_path="..\\driver\\chromedriver.exe")
#     driver.maximize_window()
#     driver.get("https://www.makemytrip.com/")
#     wait = WebDriverWait(driver, 20)
#     return driver, wait
#
#
# def test_login():
#
#     time.sleep(3)
#     WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
#         (By.CLASS_NAME, "login__card makeFlex hrtlCenter cursorPointer appendBottom10"))).click()
#
#     time.sleep(3)
#
#     # wait.until(EC.visibility_of_element_located(
#     #     (By.CLASS_NAME, "login__card makeFlex hrtlCenter cursorPointer appendBottom10"))).click()
#
#     time.sleep(3)
#     wait.until(EC.visibility_of_element_located(
#         (By.CLASS_NAME, "font14 fullWidth"))).send_keys("shivanandmishra14@gmail.com")
#
#     time.sleep(3)
#     wait.until(expected_conditions.visibility_of_element_located(
#         (By.CLASS_NAME, "capText font16"))).click()
#
#     time.sleep(3)
#     wait.until(expected_conditions.visibility_of_element_located(
#         (By.XPATH, "//input[@id='password']"))).send_keys("shiv@nand.1")
#
#     time.sleep(3)
#     wait.until(expected_conditions.visibility_of_element_located(
#         (By.CLASS_NAME, "capText font16"))).click()
#
#
# driver.quit()
