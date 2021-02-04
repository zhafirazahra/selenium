from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

passed = 0
failed = 0
timeout = 25

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://pwa.assemblrworld.com/Auth/Login')

user_input = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter email or username']")))
user_input.send_keys('zhafirazahra')

pass_input = driver.find_element_by_xpath("//input[@placeholder='Enter password']")
pass_input.send_keys('571Zahra')

driver.find_element_by_xpath("//button[@class='_1Pz2d _39bnp']").click()

try:
	element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Create project')]")))
	assert element.text == "Create project"
	# print('SignIn-00001 Test Passed')
	passed = passed+1
except AssertionError:
    print('SignIn-00001 Test Failed')
    failed = failed+1

print('\nSign In Email Test : ',passed,' Test Passed, ',failed,' Test Failed')
driver.quit()
