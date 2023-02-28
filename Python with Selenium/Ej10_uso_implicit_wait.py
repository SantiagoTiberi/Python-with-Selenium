import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #funcion para esperar un cierto momento o una condicion
from selenium.webdriver.support import expected_conditions as EC #modulo para llamar el explicit o implicit wait

class usando_unittest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r"E:\2022\chromedriver.exe")

    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #segundos
        driver.get("http://www.google.com")
        myDinaminElement = driver.find_element((By.NAME),"q") #un elemento dinamico es el cambia sus identificadores(id, name, etc) cada vez que se cargan
                                                            #lo que hace es esperar hasta que el name coincida con q si se trata de un elemento dinamico
if __name__ == '__main__':
    unittest.main()