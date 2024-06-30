from bs4 import BeautifulSoup
import requests
import time

def tickerdata(ticker):
    url = f'https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{ticker}&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'
    time.sleep(1)
    cssc = "#svdMainGrid3 > table > tbody > tr > th > div"
    cssp = "#svdMainGrid3 > table > tbody > tr > td:nth-child(3)"
    resp = requests.get(url)
    if resp.status_code == 200:
        bs = BeautifulSoup(resp.text,'html.parser')
        companys = []
        prices = []
        company = bs.select(cssc)
        price = bs.select(cssp)
        for i in range(len(company)):
            companys.append(company[i].text)
            prices.append(float(price[i].text.replace(',','')))
        l = len(companys)
        i = 0
        with open("asset_management_data.csv","a") as f:
            while i < l:
                f.write(f'{ticker},{companys[i]},{prices[i]}\n')
                i+=1

with open("asset_management_data.csv","w") as f:
    f.write("ticker,운용사명,시가평가액\n")
tickers = ["005930","000660","373220","207940","005380"]
for i in tickers:
    tickerdata(i)    


    