import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/"
resp = requests.get(url)
if resp.status_code == 200:  #200인경우 정상, 404인경우 페이지 없음
    print(resp.text)
    html = resp.text
soup = BeautifulSoup(html, 'html.parser')
result = soup.select("html")
print( type(resp) )
print(result)
