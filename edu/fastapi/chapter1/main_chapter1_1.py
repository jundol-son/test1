import uvicorn
from typing import Optional, List

from fastapi import FastAPI, Query, Path, Cookie, Header
from pydantic import BaseModel, Field, parse_obj_as ,HttpUrl

app = FastAPI()

#1. fastapi
# @app.get("/")
# def hello():
#     return "Hello, World!"

#2. fastapi 경로 매개변수
# @app.get("/users/{user_id}") # 경로 매개변수 : url경로에 들어가는 변수
# # def get_user(user_id): #문자열 응답
# def get_user(user_id: int): #정수열 응답
#     return {"user_id": user_id}

#3. fastapi 쿼리 매개변수
#웹 주소 ?뒤에 오는 값이 쿼리 매개변수
# 각 매개변수는 &로 구분되고 key=value와 같이 키/값쌍으로 정의
#아래는 limit를 쿼리 매개변수로 사용
# @app.get("/users")
# # def get_users(limit: int): # 기본값이 없으면 항상 limit값을 입력해야함 http: 8000/users?limit=100
# # def get_users(limit: int = 100): # 기본값을 추가함 http :8000/users
# def get_users(limit: int = None): # limit을 선택적으로, 기본 값 null
#     return {"limit": limit}

# 4. fastapi 요청본문1(request body)
class User(BaseModel):
    name: str
    password: str # 단순예제, 실무에서는 반드시 암호화해야함
    avatar_url: Optional[HttpUrl] = None # HttpUrl : pydantic타입


@app.post("/users")
def create_user(user: User):
    return user

#http :8000/users name=spike password=1234 name, password를 이용하여 실행
"""
답변
HTTP/1.1 200 OK
content-length: 52
content-type: application/json
date: Fri, 19 Jul 2024 06:05:47 GMT
server: uvicorn

{
    "avatar_url": null,
    "name": "spike",
    "password": "1234"
}
"""

# 4. fastapi 요청본문2(request body)
class Item(BaseModel):
    name: str
    price: float
    amount: int = 0


class User(BaseModel):
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None
    inventory: List[Item] = []  # 추가: inventory


@app.post("/users")
def create_user(user: User):
    return user


# 추가: get_user()
@app.get("/users/me")
def get_user():
    fake_user = User(
        name="FastCampus",
        password="1234",
        inventory=[
            Item(name="전설 무기", price=1_000_000),
            Item(name="전설 방어구", price=900_000),
        ]
    )
    return fake_user

# 5. 데이터 검증
# """
#  Path(), Query() 함수를 이용하면 매개변수를 명시적으로 정의할 수 있고, 다양한 옵션을 추가할 수 있음
#  Path, Query는 Params 클래스의 서브 클래스입니다. 하지만 실제로는 해당 클래스를 반환하는 함수
# """

# """
# 영어뿐만 아니라 한글도 글자 갯수를 정확하게 측정합니다. 다음 두 가지만 주의하면 됩니다.

# - `gt`, `ge`, `lt`, `le`: 숫자
# - `min_length`, `max_length`: `str`
# - `min_items`, `max_items`: 컬렉션(e.g. `List`, `Set`)

# 뿐만 아니라 `regex` 옵션으로 정규표현식 검증도 가능합니다.
# """



# inventory = (
#     {
#         "id": 1,
#         "user_id": 1,
#         "name": "레전드포션",
#         "price": 2500.0,
#         "amount": 100,
#     },
#     {
#         "id": 2,
#         "user_id": 1,
#         "name": "포션",
#         "price": 300.0,
#         "amount": 50,
#     },
# )

# # # pydantic형태
# # class Item(BaseModel):
# #     name: str
# #     price: float
# #     amount: int = 0

# # json형태로 아이템 생성(post)
# class Item(BaseModel):
#     name: str = Field(..., min_length=1, max_length=100, title="이름")
#     price: float = Field(None, ge=0)
#     amount: int = Field(
#         default=1,
#         gt=0,
#         le=100,
#         title="수량",
#         description="아이템 갯수. 1~100 개 까지 소지 가능",
#     )

# @app.post("/users/{user_id}/item")
# def create_item(item: Item):
#     return item

# @app.get("/users/{user_id}/inventory", response_model=List[Item])
# def get_item(
#     user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id"),
#     name: str = Query(None, min_length=1, max_length=2, title="아이템 이름"),
# ):
#     user_items = []
#     for item in inventory:
#         if item["user_id"] == user_id:
#             user_items.append(item)

#     response = []
#     for item in user_items:
#         if name is None:
#             response = user_items
#             break
#         if item["name"] == name:
#             response.append(item)

#     return response

# 6. 헤더,쿠키
# 1) 쿠키
# 쿠키는 사이트에서 정보 수집을 하는 프로그램이 사용하는 프로그램
# ga는 구글 애널리틱스가 사용하는 쿠키
# @app.get("/cookie")
# def get_cookies(ga: str = Cookie(None)):
#     return {"ga": ga}

#http :8000/cookie Cookie:ga=GA12.3.4
#HTTPie에서 쿠키는 Cookie:<key>=<value>;<key>=<value>와 같이 작성합니다. ;은 구분자입니다.
# 2) 헤더
# """
# 헤더에 `X-` 접두어는 사용자 정의 헤더라는 것을 의미합니다. 반드시 이렇게 할 필요는 없지만, 표준 헤더와 구분짓기 위해 사용합니다. 사실.. 이 [정책은 폐기](https://tools.ietf.org/html/rfc6648) 되었지만, 여전히 다들 이 관례를 따르고 있습니다.
# 파이썬에서 `-`을 변수명으로 허락하지 않기 떄문에, 언더스코어(`_`)를 대신 사용해야 합니다. 그리고 대소문자 구분을 하지 않습니다. 실제로는 아래와 같이 테스트하면 정상 작동합니다.
# 추가로 Header는 다른 클래스와 다르게 convert_underscores 옵션을 갖는데 False를 줄 경우 하이픈을 언더스코어로 변환하지 않습니다
# """
# @app.get("/header")
# def get_headers(x_token: str = Header(None, title="토큰")):
#     return {"X-Token": x_token}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)