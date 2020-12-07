from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
#Verify if the LOGIN element IS DISPLAYED or not
login = driver.find_element_by_id("txtUsername")
print("The login element is disabled: " , str(login.is_displayed())) #Return true or false based on the element status
print("The element is enabled or not:" +str(login.is_enabled()))
time.sleep(2)
#set user and password and click login button
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(3)
#Go to My Info tab > check if the gender IS SELECTED
driver.find_element_by_id("menu_pim_viewMyDetails").click()
print("The MALE gender is selected: ", driver.find_element_by_css_selector("#personal_optGender_1").is_selected())
print("The Feamale gender selection is : ", driver.find_element_by_id("personal_optGender_2").is_selected())
driver.quit()
# driver.quit()
