import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/board.naver?code=000810"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',    
}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html5lib')
result = soup.select('#content > div.section.inner_sub > table.type2 > tbody > tr > td.title > a')
for tag in result:
    print(tag.text.strip())