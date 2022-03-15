import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# class UtilityData:
global driver
global wait


def test_driver_data():
    global driver
    global wait
    driver = webdriver.Chrome(executable_path="..\\driver\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")
    wait = WebDriverWait(driver, 20)
    return driver, wait


test_driver_data()
