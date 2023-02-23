#Fill in a form

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#change this!
service_obj=Service("C:\\Users\\LUIS\\Downloads\\chromedriver")
driver=webdriver.Chrome(service=service_obj)

#driver.get("https://www.sopitas.com/")

driver.get("http://rahulshettyacademy.com/angularpractice/")


#ID, xPATH, CSSSelector, Classname, name, linktext
driver.find_element(By.NAME,"email").send_keys("proba@nuevos.com")
driver.find_element(By.ID,"exampleCheck1").click()

time.sleep(1000)