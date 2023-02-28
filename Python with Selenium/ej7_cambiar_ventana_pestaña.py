import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r"E:\2022\chromedriver.exe")

    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get("http://www.google.com") #abre la pagina google.com
        time.sleep(3)
        driver.execute_script("window.open('');") #es una instruccion para que se abra una pestaña web en python
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1]) #le digo que se posicione en la pestaña 1
        driver.get("http://stackoverflow.com") #carga la pagina nueva en la pestaña 1
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0]) #se regresa a la pestaña 0 (google.com)
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()