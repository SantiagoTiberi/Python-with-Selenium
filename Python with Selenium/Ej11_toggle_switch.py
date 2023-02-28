import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r"E:\2022\chromedriver.exe")

    def test_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(3)
        toggle = driver.find_element(By.XPATH,'//*[@id="main"]/label[3]/div')
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()