import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from test_Cases.home_footer_locators import *
from Input import Data_excel

# from Logging.log_file import *

# from TestCase.locators import *
# from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\shiva\\Downloads\\SDET-DevOps\\makemytrip-web-automation"
                                          "\\driver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
wait = WebDriverWait(driver, 20)

# new_row = Data_excel.row_count()
# print(new_row)
