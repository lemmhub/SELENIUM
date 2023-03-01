#Fill in a form

from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#change this!
service_obj=Service("C:\\Users\\LUIS\\Downloads\\chromedriver")
driver=webdriver.Chrome(service=service_obj)

#driver.get("https://www.sopitas.com/")

driver.get("http://rahulshettyacademy.com/angularpractice/")


#ID, xPATH, CSSSelector, Classname, name, linktext
driver.find_element(By.NAME,"name").send_keys("Bruce Wayne")
driver.find_element(By.NAME,"email").send_keys("iambatman@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("ElRobin13$")
driver.find_element(By.ID,"exampleCheck1").click()
select = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
select.select_by_index(0)
driver.find_element(By.NAME,"inlineRadioOptions").click()
driver.find_element(By.NAME,"bday").send_keys("04-12-2001")
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success").click()



time.sleep(1000)