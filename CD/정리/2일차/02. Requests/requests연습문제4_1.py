#TOP종목 추출
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://finance.naver.com/"
resp = requests.get(url)
if resp.status_code == 200:
    # print(resp.text)
    html = resp.text

soup = BeautifulSoup(html,'html.parser')
css1 = '#_topItems1 > tr > td:nth-child(2)'  #첫번째 뉴스 스크리핑
result1 = soup.select(css1)
prices = []
# for i in range(number):
#     price.append(result[i].text)

# print(price)
for price in result1:
    prices.append(price.text)

print(price)

soup = BeautifulSoup(html,'html.parser')
css2 = '#_topItems1 > tr > th > a'  #첫번째 뉴스 스크리핑
result2 = soup.select(css2)
names = []

for name in result2:
    names.append(name.text)

data = pd.DataFrame(zip(names,prices), columns=['종목','가격'])
print(data)