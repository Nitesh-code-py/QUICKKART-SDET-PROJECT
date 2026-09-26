from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# TC_01 - valid test 
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(3)
print("TC_01 Passed")

# TC_02 - invalid login (wrong password)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("password111")
driver.find_element(By.ID, "submit").click()
time.sleep(3)
print("TC_02 Passed")

# TC_03 invalid login (wrong admin)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("teacher")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "submit").click()
time.sleep(3)
print("TC_03 Passed")

# TC_04 blank username/blank password
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("")
driver.find_element(By.ID, "password").send_keys("")
driver.find_element(By.ID, "submit").click()
time.sleep(3)
print("TC_04 Passed")

# TC_05 UI check
driver.get("https://practicetestautomation.com/practice-test-login/")
user_box = driver.find_element(By.ID, "username")
pass_box = driver.find_element(By.ID, "password")
login_btn = driver.find_element(By.ID, "submit")
time.sleep(3)
print("TC_05 Passed")

driver.quit()





