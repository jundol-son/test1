from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://www.naver.com')

sel = '#shortcutArea > ul > li:nth-child(2) > a > span.service_name'
sel2 = '#shortcutArea > ul > li:nth-child(2) > a'
item = driver.find_element(By.CSS_SELECTOR, sel)
item2 = driver.find_element(By.CSS_SELECTOR, sel2)
print(item.text)
item.click()

time.sleep(30)
driver.quit()


""""
postgresql port : 5432
본인 pc인 경우 ip 127.0.0.1
"""