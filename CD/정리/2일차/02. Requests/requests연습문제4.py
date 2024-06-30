#TOP종목 추출
from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/"
resp = requests.get(url)
if resp.status_code == 200:
    # print(resp.text)
    html = resp.text

soup = BeautifulSoup(html,'html.parser')
css = '#_topItems1 > tr > td:nth-child(2)'  #첫번째 뉴스 스크리핑
result = soup.select(css)
print(result)
# number = len(result)
price = []
# for i in range(number):
#     price.append(result[i].text)

# print(price)
for ret in result:
    price.append(ret.text)

print(price)