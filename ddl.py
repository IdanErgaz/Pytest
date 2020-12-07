from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
drp= Select(driver.find_element_by_id("RESULT_RadioButton-9"))
#select by visible text
drp.select_by_visible_text("Evening") #Evning
time.sleep(2)
#select by index
drp.select_by_index(1)
time.sleep(3)
#select by value
drp.select_by_value("Radio-1")#Aftrenoon

#print all options
print("options:", len(drp.options))

allOPtions =drp.options
for option in allOPtions:
    print(option.text)

driver.quit()
