from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")

textArea1=driver.find_element_by_id("textbox").send_keys("this is my fine text file testing!!!")
driver.find_element_by_id("createTxt").click() #click on the 1st button to GENERATE the link
driver.find_element_by_id("link-to-download").click()#downlat the file after clicking on the LINK
