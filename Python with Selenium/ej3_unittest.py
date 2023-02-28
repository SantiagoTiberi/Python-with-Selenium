import unittest
from selenium import webdriver                      #es para usar el webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     #es para ser llamado del teclado y poder ingresar datos
import time                     #es para cargar los sleeps en las paginas

class usando_unittest(unittest.TestCase):
    def setUp(self): #es para inicializar el driver
        self.driver = webdriver.Chrome(executable_path=r"E:\2022\chromedriver.exe")
        
    def test_buscar(self):
        driver = self.driver
        driver.get("http://google.com")
        self.assertIn("Google", driver.title)
        elemento = driver.find_element(By.NAME,("q"))
        elemento.send_keys("selenium" + Keys.RETURN) #Keys.RETURN es otra froma de hacer ENTER
        time.sleep(5)
        assert "no se encontro el texto:" not in driver.page_source

    def tearDown(self) -> None: #es para que se termine el proceso
        self.driver.close()     #se cierra el driver

if __name__ == '__main__':
    unittest.main()         #QUIERE DECIR QUE ARRANCA DESDE EL COMIENZO DE LA CLASE