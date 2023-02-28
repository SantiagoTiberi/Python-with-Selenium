from selenium import webdriver                      #es para usar el webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     #es para ser llamado del teclado y poder ingresar datos
import time                     #es para cargar los sleeps en las paginas

driver = webdriver.Chrome(executable_path=r"E:\2022\chromedriver.exe")
driver.get("https://www.saucedemo.com/")


usuario=driver.find_element(By.ID,"user-name")#.send_keys("standard_user")
usuario.send_keys("standard_user")
#driver.find_element(By.ID,"user-name").send_keys("standard_user") #otra opcion para en usa sola linea


clave = driver.find_element(By.ID,"password")
clave.send_keys("secret_sauce")
clave.send_keys(Keys.ENTER)
#clave = driver.find_element(By.ID,"password").send_keys("secret_sauce" + Keys.ENTER) #otra opcion para en usa sola linea

time.sleep(10)
driver.close()


