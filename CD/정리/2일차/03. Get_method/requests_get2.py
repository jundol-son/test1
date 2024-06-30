import requests
from bs4 import BeautifulSoup

headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
url = "https://comic.naver.com/api/webtoon/titlelist/weekday?week=mon&order=user"
resp = requests.get(url, headers=headers)
if resp.status_code == 200:
    # print('뷰티풀' in resp.text)
    result = resp.json()
    for toon in result['titleList']:
        print(toon['titleName'])
    # print(result['titleList'])
    # print(result['titleList'][0]['titleName'])