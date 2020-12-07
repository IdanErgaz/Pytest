from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
#we need to switch to particular frame by name
#then fund the link name
#Go to state 0 by driver.switch_to .default_content()
#Now we can switch to the 2nd frame by frame name


