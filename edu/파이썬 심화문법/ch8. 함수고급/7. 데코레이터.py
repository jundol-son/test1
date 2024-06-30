"""
데코레이터 : 함수의 앞,뒤로 부가적인 기능을 넣어 주고 싶을 때 사용
- 로깅, 권한
- 클로저를 이용하여 생성
- 적용하고싶은 함수앞에 @데코레이터
- 함수 내부에서 중복을 제거하기 위하여 사용 
"""

def logger(func):
    def wrapper(arg):
        print('함수 시작')
        func(arg) #함수실행
        print('함수 끝')
    return wrapper

@logger #logger 함수에 print_hello함수를 변수로 이용
def print_hello(name):
    # print('함수 시작')
    print('hello' , name)
    # print('함수 끝')
@logger
def print_bye(name):
    # print('함수 시작')
    print('bye' , name)
    # print('함수 끝')

print_hello('startcoding')
print_bye('fastcampus')