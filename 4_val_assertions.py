#Validation assertions
import time
from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By

#FORGOT PASSWORD

service_obj = Service("/Users/LUMO/DOWNLOADS/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")


#tAG <a IS A LINK!
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
#sENDS ANOTHER PAGE

#Why do we use form????
#driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

#Writing children [2] not useful
#driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("1234")
#driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("1234")
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
#driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(100)
