from bs4 import BeautifulSoup
import requests
def get_per(code):
    url = "https://finance.naver.com/item/main.nhn?code="
    url = url+code
    resp = requests.get(url)
    if resp.status_code == 200:
        html = resp.text
    css = "#_per"
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.select_one(css)
    
    if tags:
        print(tags.text)
    else:
        print(tags)
    
print(get_per("005930"))
print(get_per("000660"))