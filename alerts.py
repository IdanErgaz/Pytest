from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.CSS_SELECTOR,".widget-content>button").click()
time.sleep(2.5)
driver.switch_to_alert().dismiss()#click DISMISS on alert
driver.find_element(By.CSS_SELECTOR,".widget-content>button").click()
time.sleep(2)
driver.switch_to_alert().accept() #click OK on alert

assert "You pressed OK!"==driver.find_element_by_id("demo").text
driver.quit()