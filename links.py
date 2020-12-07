
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.get("https://opensource-demo.orangehrmlive.com/")

links =driver.find_elements(By.TAG_NAME, "a")
print("link number:",len(links))#Number of links
for link in links:
    print(link.text)

    #cLICK ON A LINK
driver.find_element(By.CSS_SELECTOR,"#forgotPasswordLink>a").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#footer a").click()
time.sleep(5)
driver.quit()
