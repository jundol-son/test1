"""
#<div><div>Contents<div/><div/> 부모요소와 자식요소
글자와 상자(요소)
인라인요소 : 글자를 만들기위한 요소 
-> (대표적인 인라인 요소<span></span> : 수평으로 쌓임, 본질적으로 아무것도 나타내지 않는 콘텐츠 영역을 설정하는 용도)
<span style = "width :100px;">Hello</span> #인라인요소는 크기지정이 안먹힘(css안먹힘)
margin : 외부 여백 지정, padding : 내부 여백 지정
-> <span><div></div></span> : 인라인 요소 내부에는 <div>와 같은 블록 요소가들어갈 수 없음
블록요소 : 레이아웃(상자)를 만들기 위한 요소
-> (대표적인 블록 요소<div></div> 본질적으로는 아무것도 나타내지 않는, 콘텐츠 영역을 설정하는 용도, 수직으로 쌓임)
부모요소의 크기많큼 자동으로 늘어남

<head></head> : 문서의 정보를 나타내는 범위
                웹 브라우저가 해석 해야할 웹 페이지의 제목, 설명, 사용할 파일 위치, 스타일(CSS) 같은,
                웹페이지의 보이지 않는 정보를 작성하는 범위
<body></body> : 문서의 구조를 나타내는 범위
                사용자 화면을 통해 보여지는
                로고, 헤더, 푸터, 내비게이션, 메뉴, 버튼, 이미지 같은,
                웹 페이지의 보여지는 구조를 작성하는 범위
html5 : 표준 html타입 -> <!DOCTYPE html5>식으로 버전 변경 가능

    <meta charset="UTF-8"> #인코딩
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>test</title>
    <link rel="stylesheet" href=".main.css /> # rel : 가져올 문서와 관계, href : 가져올 경로
    <script src=".main.js" ></script> # src : 자바스크립트 파일을 가져오는 경우
    <script> console.log('hello world!') </script> #자바스크립트를 HTML문서 안에 작성하는 경우
    <img src='img/weather.jpg' alt ='12호태풍'/> # alt : 대체 택스트 작성
    <p></p> : 블록요소(글자를 다루는 블록요소)
    <img> : 인라인요소(이미지 삽입요소)
    <a></a> : 인라인요소(anchor) 다른/같은 페이지로 이동하는 하이퍼링크를 지정하는 요소 href : ulr위치, target= : 링크 URL의 표시 위치
    <input type="text" value="HEROPY!" placeholder="이름을 입력하세요 disable/> 
    :사용자가 데이터를 입력하는 요소, 블록요소 type=: 입력받을 데이터의 타입 value=: 미리 입력된 데이터
    placeholder 사용자가 입력할 값의 힌트, disable : 비활성화(js를 통해서 활성화가 되도록 설정)

주석 : <!--Comment-->

"""

