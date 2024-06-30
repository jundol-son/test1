import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005930"
resp = requests.get(url)
print("15.75" in resp.text)

soup = BeautifulSoup(resp.text, 'html5lib')
tag = soup.select_one('#_per')
print(tag.text)