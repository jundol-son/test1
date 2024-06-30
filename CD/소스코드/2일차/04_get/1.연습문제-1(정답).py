import requests
from bs4 import BeautifulSoup

url = "https://game.daum.net/"
resp = requests.get(url)
print('아키에이지' in resp.text)

soup = BeautifulSoup(resp.text, 'html5lib')
result = soup.select('#mArticle > div.section_game > div:nth-child(3) > div.area_pc > ul > li > a > span > strong')
for tag in result:
    print(tag.contents[0].strip())