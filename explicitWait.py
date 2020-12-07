from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\Projects\Automation\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.com/")


driver.find_elements_by_css_selector("#uitk-tabs-button-container>li")[1].click()

#set the from value to SFO
driver.find_elements_by_css_selector("[class='uitk-faux-input']")[0].send_keys("SFO", Keys.ENTER)

time.sleep(1)
#set to value to NYC
driver.find_elements_by_css_selector("[class='uitk-faux-input']")[1].send_keys("NYC", Keys.ENTER)
#set dates
# driver.find_element_by_xpath("//*[@id='d1-btn']").send_keys("11/29/2020")
#click on search
driver.find_element_by_css_selector("[data-testid='submit-button']").click()
#set Nonstop element
wait= WebDriverWait(driver,10)
# element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[2]/div[2]/div[1]/aside/fieldset/fieldset[2]/div[2]/div[1]/div[1]/div/label/span[1]")))
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div/div[2]/div[2]/div[1]/aside/fieldset/fieldset[2]/div[2]/div[1]/div[1]/div/label/span[1]")))

element.click()
time.sleep(3)
driver.quit()
