from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
source=driver.find_element_by_xpath("//*[@id='box6']")
dest=driver.find_element_by_xpath("//*[@id='box106']")
actions=ActionChains(driver)
#drag and drop sorce to destination

actions.drag_and_drop(source, dest).perform()
time.sleep(3)

driver.quit()
