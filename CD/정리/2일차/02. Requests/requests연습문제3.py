#TOP종목 추출
from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/"
resp = requests.get(url)
if resp.status_code == 200:
    # print(resp.text)
    html = resp.text

soup = BeautifulSoup(html,'html.parser')
css = '#_topItems1 > tr > th > a'  #첫번째 뉴스 스크리핑
result = soup.select(css)
# number = len(result)

# for i in range(number):
#     print(result[i].text)

for ret in result:
    print(ret.text)