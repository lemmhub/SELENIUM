
#Locators de selenium
from selenium import webdriver
import time
#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/lumo/downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#using type or value, CSS or XPATH

# CSS -  tagname[attribute='value'] -> //input[@type='submit'],  #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Enrique")
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio2']").click()
#driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

#Bringing the message
#message = driver.find_element(By.CLASS_NAME, "alert-success").text
#print(message)

#TOOL SELECTORS HUB


#Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()



time.sleep(100)












