"""
웹 구성 3요소 : HTML, CSS, JavaScripts
HTML(Hyper Text Markup Language) : 웹 페이지의 데이터를 표현하는데 사용하는 마크업 언어
CSS : 웹 페이지의 레이아웃과 스타일을 정의할 때 사용
JavaScripts : 웹 사이트에서 동적인 부분을 처리하는데 사용됨

ㅁ HTML

주요 태그 태그 설명
<html> HTML 문서임을 나타내는 태그
<head> 문서 정보, 메타 데이터, 외부 파일 정보 등을 기술
<body> 본문을 정의하는 태그로 이미지, 표, 문자를 표현
<table> 표를 정의하는 태그
<ol> 순서가 있는 목록을 표현하는 HTML 태그
<ul> 순서가 없는 목록을 표현하는 HTML 태그
<a> 클릭하면 연결될 페이지의 주소를 정의
<div> 문단을 구분
<h1>-<h6> 글자 크기 조정

- <tr> : table row
- <td> : table data
- <th> : table head (table data와 다르게 bold 채로 변경됨)

alt+shift를 이용하여 같은 줄 일괄 수정 가능 (ex. td > th 수정 시)

a 태그는 외부 문서를 연결
href : 연결할 주소를 지정
target : 링크를 클릭 시 창에 대한 설정 (Ex. target="_blank")
title : 마우스 커서를 올릴 때 도움말 설명을 설정
<a href="https://www.naver.com" target="_blank">클릭하면 네이버로 이동 </a>
_blank : 새창
_self : 기본 값으로 연결 사이트를 현재 창
_top : 모든 프레임을 제거하고 최상위 창에서 엶
_parent : 부모 창
frame name : 연결 이름의 프레임에서(언더바 없음)

줄바꿈 : <br>
문단구분 : <p>
띄어쓰기 : &nbsp

ㅁ CSS
ID : 문서 내에서 특정 요소에 유일한 식별자를 부여하는 데 사용
• 웹 개발자가 의미있는(중요한) 데이터에 이름을 부여
• 중복되는 이름의 사용 불가

CLASS : 문서 내에서 공통 요소에 식별자를 부여하는 데 사용
• 웹 개발자가 의미있는(중요한) 데이터에 이름을 부여
• 중복해서 사용 가능

Style의 지정
• 전체 구조를 rule set이라고 부름
• 각 rule set은 반드시 { }로 감싸져야 함
• 각 속성과 값의 구분은 콜론(:)을 사용
• 각 rule set에서 각 선언과 그 다음 선언을 구분하기 위해 세미콜론(;)을 사용
Ex. h1{color:blue; font-size:12px;}

선택자의 종류
1. Element selector
    선택자로 태그의 이름을 사용하는 방식
    • 주어진 HTML 문서안에서 주어진 타입의 모든 요소를 선택함
    p {color:blue;}
2. ID selector
    특정 아이디를 가진 페이지의 요소를 선택
    • 주어진 HTML 페이지에서 ID는 고유한 값
    • ID는 하나의 HTML에서 고유한 값
    • 셀렉터 자리에 #과 ID 이름을 나열
    #best {color:blue;}
3. Class selector
    클래스의 이름으로 스타일을 지정하는 방식
    • 동일한 스타일을 여러 태그에 지정할 수 있음
    • "." 과 클래스 이름을 나열
    .good {color:blue;}

↑주요 CSS Selector
• Element Selector (tag)
• ID Selector (#)
• Class Selector (.)

CSS Combinator(결합자)
결합자 종류
• 자손 (Decendant) 결합자
    공백으로 구분해서 태그의 계층 관계를 정의
    • 다수의 셀렉터를 공백으로 구분해서 선택할 태그를 구체화
        <style>
        selector-1 selector-2 {color:red;}
        </style> 
• 자식 (Child) 결합자
    ">"로 구분해서 태그의 계층 관계를 정의
    • 자기의 한 단계 아래 있는 태그만 선택
• 공백 없는 combinator (조건부 셀렉터)
    • 뒤의 속성이 앞의 속성을 수식함
    • ul.data1 : ul 태그 중에 클래스 data1을 갖는 태그
• :nth-child
    n번째 자식을 하나 선택함
    • 파라미터로 인덱스를 전달
    • 인덱스는 파이썬과 달리 1부터 시작함
    Ex. p:nth-child(2) 의 경우 p태그의 2번째가 아닌, 2번째 이며 p태그인것

table의 경우 thead와 tbody태그가 생략되어 있음

VS Code에서 Live Server 설치 시 작성한 HTML을 확인할 수 있음

미니콘다 가상환경 만들기
$ conda create –n [내 환경 이름]  ← 폴더 생성
$ conda activate [내 환경 이름]   ← 폴더 이동
$ conda deactivate [내 환경 이름] ← 폴더 해제
$ conda remove –n [내 환경 이름]  ← 폴더 삭제

크롬 F12 console에서 $$("")이용하여 내용 확인 가능
$$("#header .header_inner .shortcut_list .service_name")[3].innerText
→ 쇼핑

개발자 도구 접근이 안될 시 console창에 "allow pasting"입력

"""