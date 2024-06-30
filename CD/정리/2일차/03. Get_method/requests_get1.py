import requests
from bs4 import BeautifulSoup
def comment_page(name, code, page):
    page=page
    name = name
    code = code
    url = f"https://finance.naver.com/item/board.naver?code={code}&page={page}" #keyword뒷부분이 보기와 달라졌지만 다시 삼성으로 바꿔도 작동
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    resp = requests.get(url, headers=headers)
    css = "#content > div.section.inner_sub > table.type2 > tbody > tr > td.title > a"
    num = 1
    if resp.status_code == 200:
      bs = BeautifulSoup(resp.text,'html.parser')
      tags = bs.select(css)
      print(name, str(page)+'페이지 댓글입니다.')
      for i in tags:
        print(str(num)+'.',i.get('title'))
        num += 1

comment_page('삼성화재','000810',3)