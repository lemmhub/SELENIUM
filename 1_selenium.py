#Simple script
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Invoke browser
#Create service
#CHANGE THIS!!!!
service_obj=Service("C:\\Users\\Luis\\Downloads\\chromedriver")
driver=webdriver.Chrome(service=service_obj)


#driver.maximize_window()

driver.get("https://www.sopitas.com/")

print(driver.title)
print(driver.current_url)


#driver.back()
#driver.refresh()
#driver.forward()

#driver.close()


