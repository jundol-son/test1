import requests
from bs4 import BeautifulSoup
url = "https://www.samsungsvc.co.kr/"
resp = requests.get(url)
if resp.status_code == 200:  #200인경우 정상, 404인경우 페이지 없음
    print(resp.text)
    print("모바일" in resp.text)
    html = resp.text
# soup = BeautifulSoup(html,'html.parser')
# result = soup.select("div")
# print(len(result))
# print(result)
