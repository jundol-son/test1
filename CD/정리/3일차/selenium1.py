from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.naver.com')
sel = "#query"
sel2 = "#search-btn"
item = driver.find_element(By.CSS_SELECTOR, sel)
item2 = driver.find_element(By.CSS_SELECTOR, sel2)
item.send_keys("삼성전자")
item2.click()
time.sleep(10)
