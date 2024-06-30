"""
제너레이터 : 이터레이터를 만드는 함수
- 함수에서 yield를 사용하면 됨(return과 비교)
- 메모리 사용이 효율적이다.
"""

def season_generator(*args):
    for arg in args:
        yield arg

g = season_generator('spring','summer','autumn','winter')

print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())

def func():
    print("첫번째 작업중...")
    yield 1 # yield는 두번째, 세번째도 계속 이어갈 수 있음
    # return 1

    print('두번째 작업 중...')
    yield 2

    print('세번째 작업 중...')
    yield 3

ge = func()
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)
# print(ge) # return이용 시 retur을 만나면 함수종료