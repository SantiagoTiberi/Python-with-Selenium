import unittest
from matplotlib.pyplot import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r"E:\2022\chromedriver.exe")

#xpath es una estructura de objetos, EL RELATIVO PARTE DE UN NODO QUE NOSOTROS LE INDIQUEMOS, EL ABSOLUTO SOLO TIENE UNA RUTA Y SI SE CAMBIA DE ÑA UBICACION DEJA DE FUNCIONAR 
    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("http://google.com")
        time.sleep(3) #SE LO AGREGO PARA DARLE TIEMPO A LA PAGINA QUE SE CARGUE
        buscar_por_xpath= driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        time.sleep(3)
        buscar_por_xpath.send_keys("selenium" + Keys.ARROW_DOWN) #Keys.ARROW_DOWN es para usar la flecha hacia abajo 1 vez
        time.sleep(3)

    def tearDown(self) -> None: #CIERRA EL DRIVER
        self.driver.close()

if __name__ == '__main__':
    unittest.main()