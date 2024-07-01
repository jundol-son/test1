"""
fast api : 웹프레임워크
웹프레임워크 : spring(java), 장고, flask, sanic 등
마이크로프레임워크 : flask, sanic, fastapi -> SSR을 기본적으로 지원하지 않음, 써드파티 프로그램(react, view)을 이용하여 사용할 수 있긴 함.
                    http요청을 받고 응답해주는 것
                    SSR, admin기능, ORM등 기능이 없음 -> sqlalchemy와 같은 외부 라이브러리 사용
풀스택프레임워크 : 장고, spring -> 백앤드와 프론트앤드가 합쳐져 있음, SSR을 지원

ASGI
- WSGI 유틸리티 : 파이썬에서 지정한 웹 애플리케이션 인터페이스
                    파이썬으로 웹프레임워크를 제작하려면 WSGI를 따라야 한다.
- ASGI : WSGI와 거의 같음 + 비동기를 지원

Why fast api
- 배우기 쉽다
- 모던 파이썬 문법(파이썬 3.6 이상)
    비동기 키워드 : async, await
    타입 힌트
        js, python과 같은 동적타입 언어의 경우 변수 선언 시 타입 지정 X
        개발자에게 도움이되고 편집기에서 UI 지원이 가능
- OpenAPI 기반(+GraphQL) - swagger API : RESTful-API (REST의 원리를 따르는 API)
- 자동 문서 생성(swagger)
- 마이크로프레임워크
    API 서버
    MSA : micro service architecture
        MSA의 service를 관리하기 위한 프로그램 - 쿠버네티스
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello, World!"