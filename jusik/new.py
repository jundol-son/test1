from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Chrome 드라이버 초기화
driver = webdriver.Chrome(options=chrome_options)

# 네이버 금융 웹페이지 로드
driver.get('https://kr.investing.com/rates-bonds/usa-government-bonds?maturity_from=40&maturity_to=290')

# 페이지 로드 후 HTML 가져오기
html = driver.page_source

# BeautifulSoup으로 파싱
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 원하는 CSS 셀렉터로 요소 선택
css = '#cr1 > a'  # 예시 선택자
result = soup.select(css)

# 결과 출력
for item in result:
    print(item.text)

# 사용자의 입력을 기다림으로써 브라우저가 바로 닫히지 않게 함
input("브라우저를 닫으려면 Enter 키를 누르세요...")

# 브라우저 종료
driver.quit()