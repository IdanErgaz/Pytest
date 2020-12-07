from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
status1=driver.find_element_by_id("RESULT_TextField-1").is_displayed()
print("Field1 status is:" ,status1) #print status
status2=driver.find_element_by_id("RESULT_TextField-1").is_enabled()
print("Field1 enabled status:" ,status1) #print ENABLED status

driver.find_element_by_id("RESULT_TextField-1").send_keys("pavan")
driver.find_element_by_id("RESULT_TextField-2").send_keys("kumar")
driver.find_element_by_id("RESULT_TextField-3").send_keys("123456789")

driver.quit()



