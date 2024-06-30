import requests
from bs4 import BeautifulSoup

def get_per(ticker):
    url = f"https://finance.naver.com/item/main.nhn?code={ticker}"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, 'html5lib')
    tag = soup.select_one('#_per')
    if tag:
        return tag.text

print(get_per("005930"))
print(get_per("066570"))
print(get_per("000660"))