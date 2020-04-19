from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = wd.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    if price == True:
        button = browser.find_element_by_id("book")
        button.click()
    
    x = browser.find_element_by_id("input_value")
    x = int(x.text)
    ans = math.log(abs(12*math.sin(x)))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(ans))
    submit = browser.find_element_by_id("solve")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()