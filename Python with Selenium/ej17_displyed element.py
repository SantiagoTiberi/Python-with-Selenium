from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"E:\2022\chromedriver.exe")
driver.get("http://www.google.com")
time.sleep(5)
displayelement = driver.find_element((By.NAME),"btnI")
print(displayelement.is_displayed()) #regresa verdadero o falso si ya se cargo el elemento
print(displayelement.is_enabled()) #regresa true or false si el elemento esta disponible