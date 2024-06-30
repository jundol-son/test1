import requests
from bs4 import BeautifulSoup

url = "https://product.kyobobook.co.kr/api/gw/pub/pdt/best-seller/online?period=001&page=1&per=20&dsplDvsnCode=000&dsplTrgtDvsnCode=001"
# url = "https://product.kyobobook.co.kr/bestseller/online?period=001"
headers = {    
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

resp = requests.get(url, headers=headers)
print('오케팅' in resp.text)

data = resp.json()
for item in data['data']['bestSeller']:
    print(item['cmdtName'], item['chrcName'])
