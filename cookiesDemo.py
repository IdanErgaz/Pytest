from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.amazon.in/")


#get ALL coocies created by the browser
cookies= driver.get_cookies()
print()
print("The cookies are:", cookies)
print("SUM:", len(cookies))
for cookie in cookies:
    print(cookie)
print("----------------------------------------------------------------------------------------")
print()
#How to add a new cookie to the browser
cookie1={"name":"myCookie", "value":"123456789"}
driver.add_cookie(cookie1)
cookies=driver.get_cookies()
print()
print("We have sum after ADDING of cookies", len(cookies))#How many cookies we have after ADDING a new one?
for cookie in cookies:
    print(cookie)
print("========================================================================================")
#Delete a cookie
driver.delete_cookie('myCookie')
cookies=driver.get_cookies()
print("Sum after DELETION", len(cookies))
for cookie in cookies:
    print(cookie)
print("=============================================================================================")



#Delet all the cookies from the browser
print("Deleting ALL cookies!!!")
driver.delete_all_cookies()
print()
cookies=driver.get_cookies()
print("Current cookies:", cookies)
print("Sum:",len(cookies))
driver.quit()