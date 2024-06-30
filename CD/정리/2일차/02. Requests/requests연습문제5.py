#TOP종목 추출
from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/item/main.nhn?code=005930"
resp = requests.get(url)
if resp.status_code == 200:
    # print(resp.text)
    html = resp.text

soup = BeautifulSoup(html,'html.parser')
css = '#_per'  #per id
result = soup.select(css)
print('삼성전자의 per은' , result[0].text)
# number = len(result)
# price = []
# for i in range(number):
#     price.append(result[i].text)

# print(price)