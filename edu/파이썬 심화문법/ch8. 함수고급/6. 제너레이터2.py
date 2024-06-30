#제너레이터 표현식
double_list = [i*2 for  i in range(1,10)]
double_generator = (i*2 for  i in range(1,10)) #리스트 만드는 것에서 ()로 바꾸면 제너레이터


print(double_list)
print(double_generator)

for i in double_generator:
    print(i)

# 메모리 사용을 효율적으로 하기 위하여 사용
# ex) 숫자 1 ~ 10000 3배로 만든 결과 리스트 vs 제너레이터

import sys

lits_data = [i*3 for i in range(1,10000+1)]
generator_data = (i*3 for i in range(1,10000+1))

print(sys.getsizeof(lits_data)) #실행시 메모리 사용 정보 확인(byte)
print(sys.getsizeof(generator_data)) # 실행시 메모리 사용 정보 확인(byte)

# 리스트는 결과값을 저장, 제너레이터는 표현식만 저장, __next__를 이용하여 호출