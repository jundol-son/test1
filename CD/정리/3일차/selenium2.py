from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.investing.com/indices/us-spx-500')
sel = "#__next > div > div > div > div > div:nth-child(9) > ul > li:nth-child(1) > article > div > a"
item = driver.find_element(By.CSS_SELECTOR, sel)
print(item.text)
driver.quit()