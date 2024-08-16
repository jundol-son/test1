import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

DB_Name = 'test1'
User_Name = 'postgres'
Password = 's5764191**'
Table_Name = '시가평가액'
Host_IP = '127.0.0.1'
Port_num = '5432'
engine =create_engine(f'postgresql://{User_Name}:{Password}@{Host_IP}:{Port_num}/{DB_Name}')

url = f'https://kr.investing.com/rates-bonds/usa-government-bonds?maturity_from=40&maturity_to=290'
#pair_23697 > td.bold.left.noWrap.elp.plusIconTd > a
#pair_1199760 > td.bold.left.noWrap.elp.plusIconTd > a
#pair_23706 > td.bold.left.noWrap.elp.plusIconTd > a
#pair_23697 > td.pid-23697-last
#pair_1199760 > td.pid-1199760-last
#compBody > div.section.ul_corpinfo > div.corp_group1 > h2:nth-child(2)
#svdMainGrid3 > table > tbody > tr:nth-child(1) > th > div
cssc = "#cr1 > tbody > tr > td > a"
cssp = "#svdMainGrid3 > table > tbody > tr > td:nth-child(3)"
resp = requests.get(url)
tickers =[]
companys = []
prices = []
if resp.status_code == 200:
    bs = BeautifulSoup(resp.text,'html.parser')
    company = bs.select(cssc)
    price = bs.select(cssp)
    for i in range(len(company)):
        companys.append(company[i].text)
        prices.append(float(price[i].text.replace(',','')))
    df = pd.DataFrame({'tickers':'005930','운용사명':companys,'가격':prices})
print(df)

driver = webdriver.Chrome()

driver.get('https://kr.investing.com/rates-bonds/usa-government-bonds?maturity_from=40&maturity_to=290')
# element = driver.find_element(By.CSS_SELECTOR, '#content > div.article2 > div.section1 > div.group3 > a > em').click()


# 브라우저를 유지시키기 위해 사용자의 입력을 기다림
input("브라우저를 닫으려면 Enter 키를 누르세요...")