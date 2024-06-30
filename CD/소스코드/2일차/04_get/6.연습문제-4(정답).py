import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/campaigns/82"
headers = {
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',    
}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html5lib')
tag = soup.select_one('a > dl > dd > div.name')
print(tag.text)
