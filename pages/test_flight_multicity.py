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

# close banner
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[@class='langCardClose']"))).click()


wait.until(expected_conditions.visibility_of_element_located((By.XPATH, log_in))).click()
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "T&Cs"))).click()
scroll_to_top = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "APPLICABILITY")))
action = ActionChains(wait)

driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
driver.find_element(By.ID, "header_tab_flights").click()


self.driver = driver

# select multi city
wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "(//span[@class='tabsCircle appendRight5'])[3]"))).click()

try:
    # from
    wait.until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//label[@for='fromAnotherCity0']"))).click()
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='From']"))).send_keys("PNQ")
    time.sleep(2)
    assert "Pune" == "Pune"
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[contains(.,'Pune, India')]"))).click()

    # to
    wait.until(
        expected_conditions.visibility_of_element_located((By.XPATH, "(//span[contains(.,'To')])[1]"))).click()
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='To']"))).send_keys("DEL")
    time.sleep(2)
    assert "Delhi" == "Delhi"
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[contains(.,'Delhi, India')]"))).click()

    # Calendar
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "(//div[@class='dateInnerCell'])[26]"))).click()

    # another from
    wait.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//label[@for='fromAnotherCity1']"))).click()
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='From']"))).send_keys("CCU")
    time.sleep(2)
    assert "Kolkata" == "Kolkata"
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[contains(.,'Kolkata, India')]"))).click()

    # another to
    # wait.until(
    #     expected_conditions.visibility_of_element_located((By.XPATH, "(//span[contains(.,'To')])[3]"))).click()
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='To']"))).send_keys("HYD")
    time.sleep(2)
    assert "Hyderabad" == "Hyderabad"
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[contains(.,'Hyderabad, India')]"))).click()

    # Calendar
    # wait.until(expected_conditions.visibility_of_element_located(
    #     (By.XPATH, "//label[@for='anotherDeparture 1']"))).click()
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//p[normalize-space()='31']"))).click()

    #     Add another  and remove city
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "(//button[@data-cy='addAnotherCity'])[2]"))).click()
    time.sleep(2)
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//span[@data-cy='removeCity-2']"))).click()

    # Select a fare type
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "(//li[@class='font12 blackText latoBold wrapFilter  '])[1]"))).click()

    # Search
    driver.implicitly_wait(2)
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH,
         "//a[@class='primaryBtn font24 latoBold widgetSearchBtn disableSearch widgetSearchBtnMultiCity']"))).click()

except TimeoutException:
    print("YOU link not found ... breaking out")
