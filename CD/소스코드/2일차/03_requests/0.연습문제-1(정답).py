import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html5lib')
tag = soup.select_one('#content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li:nth-child(1) > span > a')
print(tag.text)
tag = soup.select_one('#content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li:nth-child(2) > span > a')
print(tag.text)
tag = soup.select_one('#content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li:nth-child(3) > span > a')
print(tag.text)
tag = soup.select_one('#content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li:nth-child(4) > span > a')
print(tag.text)
tag = soup.select_one('#content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li:nth-child(5) > span > a')
print(tag.text)

result = soup.select('#content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li > span > a')
for tag in result:
    print(tag.text)