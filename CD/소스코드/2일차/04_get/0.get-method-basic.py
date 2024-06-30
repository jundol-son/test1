import requests
from bs4 import BeautifulSoup

url = "https://browse.gmarket.co.kr/search?keyword=%EC%82%BC%EC%84%B1"
resp = requests.get(url)
print("삼성전자" in resp.text)

sel = "#section__inner-content-body-container > div:nth-child(5) > div:nth-child(1) > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item"
soup = BeautifulSoup(resp.text, 'html5lib')
tag = soup.select_one(sel)
print(tag.text)