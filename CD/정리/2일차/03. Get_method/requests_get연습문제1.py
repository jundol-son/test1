import requests
from bs4 import BeautifulSoup

url = "https://www.gmarket.co.kr/n/search?keyword=%EC%82%BC%EC%84%B1" #keyword뒷부분이 보기와 달라졌지만 다시 삼성으로 바꿔도 작동
url = "https://www.gmarket.co.kr/n/search?keyword=삼성"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

resp = requests.get(url, headers=headers)
css = "#section__inner-content-body-container > div:nth-child(4) > div > div > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong"
if resp.status_code == 200:
    bs = BeautifulSoup(resp.text, 'html.parser')
    tags = bs.select(css)
    for i in tags:
        print(i.text)
