import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/board.naver?code=000810"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',    
}

resp = requests.get(url, headers=headers)
print('급등은' in resp.text)

# soup = BeautifulSoup(resp.text, 'html5lib')
# tag = soup.select_one('a > dl > dd > div.name')
# print(tag.text)