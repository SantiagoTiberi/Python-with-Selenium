import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #funcion para esperar un cierto momento o una condicion
from selenium.webdriver.support import expected_conditions as EC #condicion para que prociga con la automatizacion

class usando_unittest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r"E:\2022\chromedriver.exe")

    def test_usando_explicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")
        try: #se le opone intentos en vez de un time.sleep
            element = WebDriverWait(driver, 10).until(              #intenta encontrar 10 veces hasta que el elemento "q" se presente
                EC.presence_of_element_located((By.NAME, "q"))
                )
        finally:
            driver.quit() #se cierra el driver

if __name__ == '__main__':
    unittest.main()