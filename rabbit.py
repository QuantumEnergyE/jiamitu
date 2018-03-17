import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://jiamitu.mi.com/lottery/turntable")
user = driver.find_element_by_id("username")
user.clear()
user.send_keys("your_name")

pwd = driver.find_element_by_id("pwd")
pwd.clear()
pwd.send_keys("your_pwd")

login = driver.find_element_by_id("login-button")
login.send_keys(Keys.RETURN)

WebDriverWait(driver, 5).until(EC.staleness_of(login))

img = driver.find_element_by_class_name("pointer")
img.click()

while 1:
    img.click()
    btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn')))
    btn.click()
    while btn.is_displayed():
        time.sleep(1)