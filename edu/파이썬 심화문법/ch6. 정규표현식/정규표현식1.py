""""
정규표현식 장점
- 문자열 추출, 유효성검사에 유용하게 쓰일 수 있다.
- 거의 모든 언어에서 사용가능
정규표현식 단점
- 가독성이 좋지 못하며, 유지보수가 힘들다

정규표현식 연습사이트 : https://regexr.com/639t5

정규표현식 사용방법
1) Flags
2) Character classes
3) Anchors
4) Escape Characters

re모듈
match : 문자열 처음부터 검색
찾는경우 : match object 1개, 없는경우 : None
- match(regex,문자열)
serch : 문자열 전체 검색
찾는경우 : match object 1개, 없는경우 : None
- findall
찾는경우 : 문자열 리스트, 없는경우 : 빈리스트
- finditer
찾는경우 : match object iterator, 없는경우 : None
-fullmatch : 패턴과 문자열이 남는 부분없이 완벽히 일치
찾는경우 : match object 1개, 없는경우 : None

match 객체의 메서드
group : 매칭된 문자열 반환
start : 시작위치
end : 끝의 위치
span : 매칭된 문자열의 (시작,끝) 튜플

"""

import re
str = 'love people around you, love yout work, love yourself'

#1) match : 문자열의 처음부터 검색
result = re.match('love',str)
print(result)
#2) search : 문자열의 처음부터 검색
result = re.search('love',str)
print(result)
#3) findall : 문자열의 처음부터 검색
result = re.findall('love',str)
print(result)
#4) finditer : 문자열의 처음부터 검색
results = re.finditer('love',str)
for result in results:
    print(result)  
#5) fullmatch : 문자열의 처음부터 검색
str2 = 'Hey Guys, read books'
result = re.fullmatch('.*',str2)
print(result)

# 2. match object의 메서드
result = re.search('people', str)

# 1) group()
print(result.group())
# 2) start()
print(result.start())
# 3) end()
print(result.end())
# 4) span()
print(result.span())