"""
이터러블 객체 : 순서가 있는 자료형
 - 문자열, 리스트, 튜플, 딕셔너리, range 객체
 - for i in '이터러블 객체'

 이터레이터 클래스 정의
 __iter__, __next__ 객체 정의
"""
for i in "123":
    print(i)

for i in [10,20,30]:
    print(i)

print(print([10,20,30]))
print(type([10,20,30]).__iter__)

iter_obj = [10,20,30].__iter__() # 메서드가 어떻게 동작하는지 알 수 있음
print(iter_obj)

# for i in iter_obj:
#     print(i)

# print(dir(iter_obj))
print(iter_obj.__next__()) # 10
print(iter_obj.__next__()) # 20
print(iter_obj.__next__()) # 30
print(iter_obj.__next__()) # StopIteration