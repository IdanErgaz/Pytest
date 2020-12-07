#See 4:21 :21 at the video https://www.youtube.com/watch?v=o3tYiyE_OXE
import XLUtils
from selenium import webdriver


driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
path="C:\BIGFIX\login.xlsx"

rows=XLUtils.getRowCount(path, 'Sheet1')

for r in range(2,rows+1):
    username=XLUtils.readDate(path, 'Sheet1', r, 1)
    password=XLUtils.readDate(path, 'Sheet1', r, 2)

    driver.find_element_by_name("txtUsername").send_keys(username)
    driver.find_element_by_name("txtPassword").send_keys(password)
#click the submit button
    driver.find_element_by_name("Submit").click()

    if (driver.find_element_by_css_selector(".box h1").text=="Dashboard"):
        print("test is passed!")
        XLUtils.writeData(path, 'Sheet1', r, 3, "Test passed!!!")
    else:
        print("Test failed!")
        XLUtils.writeData(path, 'Sheet1', r, 3, "Test FAILED!!!")
    # driver.find_element_by_id("welcome").click()
    # driver.find_element_by_link_text("Logout")
