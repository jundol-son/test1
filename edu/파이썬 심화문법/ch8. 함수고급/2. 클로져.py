"""
1. 내부함수 : 함수안에서 정의되는 함수
2. 클로져 : 함수가 종료되어도 자원(변수)를 사용할 수 있는 함수
 - 클로저가 될 3가지 조건
    1) 내부함수 2) 외부함수의 변수를 참조 3) 외부함수가 내부함수를 반환해야 한다.
"""
# 내부함수(inner)와 외부함수(outer)
def outer(name):
    def inner():
        print(name, "님 안녕하세요!")
    return inner #일급객체

func = outer("startcoding")
func() #inner가 클로져


def greeting(name, age, gender):
    def inner():
        print(name, "님 안녕하세요!")
        print('나이:', age)
        print('성별:', gender)
    return inner

closure = greeting('나미', 27, 'female')
closure()

# dir(closure) #클로져 객체 내부 확인
# print(dir(closure.__closure__[0])) #'cell_contents라는 속성이 보임
# print((closure.__closure__[0]).cell_contents)

for i in closure.__closure__:
    print(i.cell_contents)

# 전역변수를 사용하여 대체 가능
# ex. name = OO
# 전역변수 사용을 최소화 하는 것이 좋음(네이밍문제, 스코프문제)
# class를 이용하여 대체 가능
