from selenium import webdriver
from selenium.webdriver.common.by import By
import time
fp=webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")  #mime type
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "C:\BIGFIX")
fp.set_preference("browser.download.folderList", 2);
fp.set_preference("pdfjs.disabled", True)


driver=webdriver.Firefox(executable_path="C:\Projects\Automation\Drivers\geckodriver.exe",
                         firefox_profile=fp)

driver.get("http://demo.automationtesting.in/FileDownload.html")

#download the text file
textArea1=driver.find_element_by_id("textbox").send_keys("this is my fine text file testing!!!")
driver.find_element_by_id("createTxt").click() #click on the 1st button to GENERATE the link
driver.find_element_by_id("link-to-download").click()#downlat the file after clicking on the LINK

#quit
driver.quit()