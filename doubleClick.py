from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

button= driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")

actions=ActionChains(driver)
# double click operation
actions.double_click(button).perform()
driver.quit()