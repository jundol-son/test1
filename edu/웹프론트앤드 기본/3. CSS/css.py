"""
선택자{속성1:값1; 속성2:값2;}
주석 : /*설명작성*/

선택자 : 기본, 복합, 가상클래스, 가상 요소, 속성
- 기본
    전체선택자 : * , 모든요소를 선택
    태그선택자 : 태그이름, 태그이름이 동일한 요소를 선택
    클래스선택자 : .이름, class 속성의 값이 '이름'인 요소 선택
    아이디선택자 : #이름, id 속성의 값이 '이름'인 요소 선택
- 복합
    일치선택자 : ABCXYZ, 선택자 ABC와 XYZ를 동시에 만족하는 요소 선택
                span.orange : span 태그이며, class가 orange인 요소
    자식선택자 : ABC>XYZ, 선택자 ABC의 자식요소 XYZ 선택.
                ul> .orange : ul태그의 자식이며 class가 orange인 요소
    하위(후손)선택자 : ABC XYZ, 선택자 ABC의 후손요소 XYZ 선택.
                div .orange : div요소의 후손 이며 class가 orange인 요소
    인접 형제 선택자 : ABC + XYZ, 선택자 ABC의 다음 형제 요소 XYZ 하나를 선택
                .orange + li : 클래스 orange의 다음 li 형제 요소 선택
    일반 형제 선택자 : ABC ~ XYZ, 선택자 ABC의 다음 형제 요소 XYZ 모두를 선택
                .orange ~ li : 클래스 orange의 다음 li 형재 요소 모두 선택
- 가상클래스
    HOVER : ABC:hover , 선택자 ABC 요소에 마우스 커서가 올라가 있는 동안 선택
                a:hover{color:red;} : a요소에 마우스 커서가 올라가 있으면 빨간색으로 변함
    ACTIBE : ABC:active , 선택자 ABC 요소에 마우스를 클릭하고 있는 동안 선택.
                a:active{color:red;} : a요소에 마우스를 클릭하고 있는 동안 빨간색으로 변함
    FOCUS : ABC:focus , 선택자 ABC요소가 포커스되면 선택(input요소 입력창에 마우스를 올려놓은게 포커스) - 포커스된 상태에서 바깥 화면을 클릭(blur) - 포커스 해제
                a:focus{backgroud=color:orange;} : input입력창에 마우스를 올리면 입력창 배경이 오렌지 색으로 변함
    FIRST CHILD : ABC:first-child, 선택자 ABC가 형제 요소 중 첫째라면 선택
                .fruits span:first-child{color :red;}
    LAST CHILD : ABC:last-child, 막내 선택
                .fruits h3:last-child{color :red;}
    NTH CHILD : ABC:nth-child(n), nth-child 선택
- 가상 요소
    BEFORE : ABC::before, 선택자 ABC 요소의 내부 앞에 내용(content)을 삽입. -인라인 요소
                .box::berfore{content : "앞!";} : box내부 앞에 "앞!"내용이 삽입됨
    AFTER : ABC::AFTER, 선택자 ABC 요소의 내부 뒤에 내용(content)을 삽입. - 인라인 요소
                .box::AFTER{content : "뒤!";} : box내부 뒤에 "뒤!"내용이 삽입됨
- 속성
    ATTR : [ABC] 속성 ABC을 포함하는 요소 선택
                [disabled]{color: red;} disabled라는 속성을 가진 요소만 빨간색으로 변함
    ATTR=VALUE : [ABC='XYZ'] 속성 ABC을 포함하고 값이 XYZ 요소 선택
                [type="password"]{color: red;} type 속성이 password인 요소 빨간색으로 변함
"""