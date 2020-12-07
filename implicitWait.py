from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

#wait for max 10 second untill page is loaded
driver.implicitly_wait(10)
assert "OrangeHRM" in driver.title
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(3)
driver.quit()
