import time

import self as self
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import ActionChains
from locators.practice_locators import *

driver = webdriver.Chrome(executable_path="..//driver//chromedriver.exe")
wait = WebDriverWait(driver, 20)
driver.get("https://www.makemytrip.com/")
driver.maximize_window()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, log_in))).click()
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "T&Cs"))).click()
scroll_to_top = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "APPLICABILITY")))
action = ActionChains(wait)

driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
driver.find_element(By.ID, "header_tab_flights").click()

self.driver = driver
try:
    # to
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='fromCity']"))).click()
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@aria-autocomplete='list']"))).send_keys("BLR")
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[contains(.,'Bengaluru, India')]"))).click()

    # from
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='toCity']"))).click()
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@aria-autocomplete='list']"))).send_keys("IXD")
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[contains(.,'Allahabad Airport')]"))).click()

except TimeoutException:
    print("YOU link not found ... breaking out")

# calendar
# Departure date selection
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//div[@class='dateInnerCell'])[25]"))).click()

# Return date selection
wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "//p[@data-cy='returnDefaultText']"))).click()
wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "(//div[@class='dateInnerCell'])[32]"))).click()

# traveller and class
wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "//span[contains(@class,'lbl_input latoBold appendBottom5')]"))).click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//li[@data-cy='adults-2']"))).click()
wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "//button[@data-cy='travellerApplyBtn']"))).click()

# Search
wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']"))).click()

