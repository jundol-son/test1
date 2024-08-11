#beatifulsoup을 이용하여 미국국채금리를 크롤링 하려고함
#자바스크립트를 이용한 동적 페이지라 요소를 확인하기 어려움

import requests
from bs4 import BeautifulSoup

url = 'https://kr.investing.com/markets/united-states'

# 올바른 셀렉터
cssp = "tr#pair_23701 td a"
resp = requests.get(url)

if resp.status_code == 200:
    bs = BeautifulSoup(resp.text, 'html.parser')
    a = bs.select_one(cssp)
    if a:
        print(a.text)
    else:
        print("해당 요소를 찾을 수 없습니다.")
else:
    print(f"요청 실패: 상태 코드 {resp.status_code}")