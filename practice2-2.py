from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = wd.Chrome()
    browser.get(link)
    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    #confirm = browser.switch_to.alert
    #confirm.accept()
    x = browser.find_element_by_id("input_value")
    x = int(x.text)
    ans = math.log(abs(12*math.sin(x)))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(ans))
    submit = browser.find_element_by_xpath("/html/body/form/div/div/button")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()