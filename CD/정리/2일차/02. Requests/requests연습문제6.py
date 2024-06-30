#TOP종목 추출
from bs4 import BeautifulSoup
import requests

# url1 = "https://finance.naver.com/item/main.nhn?code=005930" #삼성전자
# url2 = "https://finance.naver.com/item/main.nhn?code=000660" #하이닉스
url = "https://finance.naver.com/item/main.nhn?code="

def get_per(name,code,css):
    code = code
    css = css
    name = name
    resp = requests.get(url+code)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text,'html.parser')
    try:
        result = soup.select(css)
        print(name+'의 per은',result[0].text)
    except:
        print(name+'의 per은','None')

get_per('삼성전자','005930','#_per')
# get_per('하이닉스','000660','#tab_con1 > div:nth-child(5) > table > tbody:nth-child(2) > tr > td > em:nth-child(1)')
get_per('하이닉스','000660','#_per')
