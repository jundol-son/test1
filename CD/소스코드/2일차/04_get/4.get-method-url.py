import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/api/home/component?type=DAILY_WEBTOON&order="
resp = requests.get(url)
print('사랑,' in resp.text)

result = resp.json()
print(result['titleList'][0]['titleName'])
