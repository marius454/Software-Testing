from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import pytest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test")
    browser = wd.Chrome()
    yield browser
    print("\nquit browser")
    time.sleep(2)
    browser.quit()

class TestForm():
    def collect_fields(self, browser, link):
        browser.get(link)
        self.div1 = browser.find_element_by_class_name("first_block")
        self.input1 = self.div1.find_elements_by_class_name("form-control")

        self.div2 = browser.find_element_by_class_name("second_block")
        self.input2 = self.div2.find_elements_by_class_name("form-control")
        self.button = browser.find_element_by_class_name("btn-default")
    
    def send_keys(self):
        self.input1[0].send_keys("Vardenis")
        self.input1[1].send_keys("Paverdenis")
        self.input1[2].send_keys("VardPav@RealMail.net")
        self.input2[0].send_keys("123546789")
        self.input2[1].send_keys("adress st. 1-23")
        self.button.click()

    def test_correct_form(self, browser):
        print("start test with correct link")
        self.collect_fields(browser, link1)

        assert len(self.input1) == 3, "Missing or too many fields"
        self.send_keys()
    
    def test_incorrect_form(self, browser):
        print("start test with incorrect link")
        self.collect_fields(browser, link2)

        assert len(self.input1) == 3, "Missing or too many fields"
        self.send_keys()
