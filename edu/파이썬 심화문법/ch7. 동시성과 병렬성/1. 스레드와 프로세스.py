"""
프로그램 : 작업을 수행하는 명령어 집합
프로세스 : 실행중인 프로그램
스레드 : 프로세스에서 실행되는 작업
프로세스는 기본적으로 하나의 스레드로 구성되지만, 경우에 따라 여러 개의 스레드로 구성가능(멀티스레딩)
동시성 : 스레드 전환이 아주 빠르게 일어나서 동시에 일어나는 것 처럼 보임

멀티 프로세싱 : core가 여러개로 프로세스를 여러개 동시에 진행(진짜 동시에 진행)
병렬성 : 멀티 프로세싱을 이용하여 동시에 실행되는 것
자원소모 : 멀티프로세싱 > 멀티 스레딩
"""
import threading

# 스레드에서 실행할 함수
def work():
    print("[sub] start")
    keyword = input("[sub] 검색어를 입력하세요 >>>")
    print(f'[sub] {keyword}로 검색을 시작합니다...')
    print("[sub] end")

# 메인스레드 실행 부분
print("[main] start")

worker = threading.Thread(target=work) #쓰레드 모듈에서 실행할 인자(work)
# worker.daemon = True #메인스레드가 종료될때 sub스레드도 같이 종료
worker.start()

print("[main] 메인 스레드는 자기할일을 합니다..")
print("[main] end")
