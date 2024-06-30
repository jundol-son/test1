from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/"
resp = requests.get(url)
if resp.status_code == 200:
    # print(resp.text)
    html = resp.text

soup = BeautifulSoup(html,'html.parser')
css = 'div.section_strategy > ul > li:nth-child(1)'  #첫번째 뉴스 스크리핑
css = 'div.section_strategy > ul' #뉴스제목 전체 스크리핑
result = soup.select(css)
# print(result[0].text)

# for ret in result:
#     print(ret)
#     print(ret.text)

#강사님 답변
# import requests
# from bs4 import BeautifulSoup
# url = "https://finance.naver.com"
# css = "#content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li > span > a"
# css = ".home .article .news_area .section_strategy ul li a"  #style
# css = "#content .news_area li a"
# resp = requests.get(url)
# if resp.status_code==200:
#   #print("코스피" in resp.text)
#   bs = BeautifulSoup(resp.text, "html.parser")
#   result = bs.select(css)
#   print(result)
#   for ret in result:
#     print(ret)
#     print(ret.text)