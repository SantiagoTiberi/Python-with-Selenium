from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"E:\2022\chromedriver.exe")
driver.get("http://python.org")
driver.close()