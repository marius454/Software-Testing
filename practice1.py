from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

link = "https://admin.typeform.com/signup"

try:
    browser = wd.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.ID,"name")
    input1.send_keys("Mr. Robot")
    input2 = browser.find_element(By.ID,"email")
    input2.send_keys("realEmail@RealMail.net")
    input3 = browser.find_element(By.ID,"password")
    input3.send_keys("drowssap")
    checkbox1 = browser.find_element(By.ID,"terms")
    checkbox1.click()
    checkbox1.click()
    checkbox2 = browser.find_element(By.ID,"consents")
    checkbox2.click()
    button = browser.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[2]/div[2]/div[2]/div/form/div[8]/div/button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()