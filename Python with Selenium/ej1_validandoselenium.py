from selenium import webdriver
#import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
#time.sleep(3)
driver.get("http:\\python.org")
driver.close()
