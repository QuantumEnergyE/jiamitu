from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://jiamitu.mi.com/home")
user = driver.find_element_by_id("username")
user.clear()
user.send_keys("your_name")

pwd = driver.find_element_by_id("pwd")
pwd.clear()
pwd.send_keys("your_pwd")

login = driver.find_element_by_id("login-button")
login.send_keys(Keys.RETURN)

WebDriverWait(driver, 5).until(EC.staleness_of(login))

btn = driver.find_element_by_xpath("//button[1]")

while 1:
        btn.click()
