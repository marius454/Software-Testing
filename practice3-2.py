from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import unittest

#link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"


class TestForm(unittest.TestCase):

    def setUp(self):
        self.browser = wd.Chrome()
        self.browser.get(link)

        self.div1 = self.browser.find_element_by_class_name("first_block")
        self.input1 = self.div1.find_elements_by_class_name("form-control")

        self.div2 = self.browser.find_element_by_class_name("second_block")
        self.input2 = self.div2.find_elements_by_class_name("form-control")
        self.button = self.browser.find_element_by_class_name("btn-default")

    def test_form(self):
        self.assertEqual(len(self.input1), 3, msg="Missing or too many fields")
        self.input1[0].send_keys("Vardenis")
        self.input1[1].send_keys("Paverdenis")
        self.input1[2].send_keys("VardPav@RealMail.net")
        self.input2[0].send_keys("123546789")
        self.input2[1].send_keys("adress st. 1-23")
        self.button.click()

    def tearDown(self):
        time.sleep(2)
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()