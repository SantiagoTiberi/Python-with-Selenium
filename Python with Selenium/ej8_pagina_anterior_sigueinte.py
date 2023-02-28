import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r"E:\2022\chromedriver.exe")

    def test_pagin_sig_o_ant(self):
        driver= self.driver
        driver.get("http://www.gmail.com")
        time.sleep(3)
        driver.get("http://www.youtube.com")
        time.sleep(3)
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()