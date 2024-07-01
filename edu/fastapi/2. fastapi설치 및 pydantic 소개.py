"""
프로젝트 디렉토리 생성
    터미널
    mkdir {디렉토리}
    cd {디렉토리}

flake 8 린터

실행방법
- 장고와 플라스크의 경우 python main.py와 같이 실행하면 작동 - 각 프레임워크마다 개발용 서버를 내장하고 있기 때문
- 많은 초보 개발자들이 개발용 서버를 상용 배포 하는 실수 - 내장서버, 웹서버, WAS를 구분 못하는 개발자 발생
- FAST API는 개발서버를 삭제 - uvicorn이라는 실제 서버를 사용하여야 함.

실행 : uvicorn main:app
        main : main.py
        app : main.py에서 app 모듈
실행 : uvicorn main:app --reload
        --reload : 파일에 변화가 생기면 재시작
uvicorn으로 실행이 번거로운 경우 마지막에
if __name__=="__main__":
    uvicorn.run("main:app", reload=True)

서버에 /docs를 이용하면 swagger로 이동
redoc으로 이동하면 대체 문서 제공 - 실제 테스트가 어려워 활용을 잘 안함

fast api설치시 starlette,pydantic라이브러리 자동설치
starlette : fastapi가 사용하는 웹 프레임워크
pydantic : 데이터 검증 라이브러리 (marshmallow와 비슷함)
            단순히 타입 검사를 하는 것이 아니라 적절하게 변형(cast)해줌
            예) GET/user/123을 호출할 때 실제로 123은 문자열이지만, 웹 애플리케이션에서는 정수형/문자열인지 판단어려움
                이 때 pydantic을 사용하여 개발자가 원하는 타입으로 받을 수 있음


"""
