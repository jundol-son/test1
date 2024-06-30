"""
1. BeautifulSoup
html을 토대로 parsing

VS CODE꿀팁
key board shortcut 확인 = 단축키 모음 및 수정가능
복사 위 alt+shift+↑
control with out debuging = ctrl + F5
화면분할 ctrl + \

파이썬에서 ctrl+/를 이용하였을때 주석처리가 안되는경우 한컴 입력기 때문일 수 있음
ctrl+shift를 눌러 전환가능


2. Requests
• 파이썬에서 HTTP 요청을 쉽게 보낼 수 있도록 설계된 라이브러리
• https://requests.readthedocs.io/en/latest/

(1.requests(html받아오기) ▶ beautifulsoup(html로 부터 parsing))
requests로 조회한 HTML을 BeautifulSoup으로 전달
resp = requests.get(url)
soup = BeautifulSoup( resp.text, 'html.parser' )
tag = soup.select_one('tag')
print(tag.text)

• JSON으로 값을 반환하는 예제
• 데이터를 쉽게 "교환"하고 "저장"하기 위한 텍스트 기반의 데이터 교환 표준

Get 메서드
서버로 요청하는 데이터의 정보를 URL로 표현
• URL의 값을 변경하면 다른 페이지로 이동
• 웹 페이지를 분석해서 변수와 값을 알아내야 함
? : URL과 데이터를 구분
= : 변수와 값을 구분
& : 데이터와 데이터를 구분
https://n.news.naver.com/mnews/hotissue/article/029/0002883161?type=series&cid=1088170
url : https://n.news.naver.com/mnews/hotissue/article/029/0002883161
데이터 : type=series&cid=1088170
type=series
cid=1088170

여러 텍스트가 있는 경우 contents를 이용하여 슬라이싱하여 추출 가능

Header가 필요한 경우
개발자도구 - Network를 이용하여 Header추출 가능

• requests의 headers 파라미터로 값 전달
• { key1: value1, key2: value2 } 형태로 추가
• 필수적인 값들이 무엇인지 사용하면서 찾아야 함

headers = {
"": ""
}
headers = {
 'User-Agent': 'Mozilla/5.0 ...', 
}
resp = requests.get(url, headers=headers)
print('급등은' in resp.text)

3. JSON
JSON(JavaScript Object Notation)은 경량의 데이터 교환 형식
• 인간이 읽을 수 있을 만큼 간단하면서도, 기계가 파싱하고 생성하기 쉽게 설계
• 주로 웹 애플리케이션에서 서버와 클라이언트 간 데이터를 전송할 때 사용
리스트와 딕셔너리의 혼합으로 되어있음

4. 정적 웹 페이지와 동적 웹 페이지
정적 웹 페이지
• 서버에 저장된 파일이 그대로 사용자에게 전달
• 변경되지 않는 내용(회사 소개, 랜딩 페이지, 포트폴리오, 문서, 블로그)을 표현하기에 적합
• 일반적으로 빠르게 데이터를 로드
    웹 브라우져 == Response 객체
    
동적 웹 페이지
• 서버 또는 클라이언트에서 실시간으로 컨텐츠를 생성
• 사용자의 요청이나 상호작용에 따라 컨텐츠를 생성 및 변경
    웹 브라우져 != Response 객체

Ajax (Asynchronous JavaScript and XML)
    웹 페이지가 서버와 백그라운드에서 데이터를 교환하고
    동적으로 일부를 업데이트하는 기술이다. 이를 통해
    페이지 전체를 새로고침하지 않고 웹 페이지의 일부분만을
    업데이트한다.

웹페이지 구조 정리
    • 서버마다 데이터를 전달하는 방식이 다름
    • 정적 로딩 / 동적 로딩
    • Get / Post
    • HTML / JSON
    • 웹 서버를 분석하고 적절한 url로 데이터를 request

스크래핑 과정 정리
패킷검색 → 헤더분석(URL/Method) → get/post(payload분석) → Request → BeautifulSoup/Json
"""