from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
#db접근을 위한 내용
DB_Name = 'test1'
User_Name = 'postgres'
Password = 's5764191**'
Table_Name = '시가평가액'
Host_IP = '127.0.0.1'
Port_num = '5432'
engine =create_engine(f'postgresql://{User_Name}:{Password}@{Host_IP}:{Port_num}/{DB_Name}')
#스크래핑
url = f'https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'
cssc = "#svdMainGrid3 > table > tbody > tr > th > div"
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
    # with open("asset_management_data.csv","w") as f:
    #     f.write("ticker,운용사명,시가평가액\n")
    #     while i < l:
    #         f.write(f'005930,{companys[i]},{prices[i]}\n')
    #         i+=1
#db에 저장
df.to_sql('test_dvb', engine, if_exists='replace', index=False)
#db에서 불러오기
query = "SELECT*FROM test_dvb;"
result_df = pd.read_sql_query(query, engine)
print(result_df)