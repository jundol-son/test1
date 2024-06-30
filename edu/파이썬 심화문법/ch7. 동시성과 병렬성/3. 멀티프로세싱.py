import multiprocessing as mp

#프로세스에서 실행할 함수

def sub_process(name):
    print("[sub] start")
    print(name)
    cp = mp.current_process()  # process의 id 출력하는 기능
    print(f'[main] pid : {cp.pid}')
    print("[sub] end")

#메일 프로세스

if __name__ == "__main__": #메인 모듈일 경우에만 실행해라
    print("[main] start")
    p = mp.Process(target=sub_process, args=('startcoding',)) #args 가변인자 형태로 sub_process의 name에 넘겨줌
    p.start()
    cp = mp.current_process()
    print(f'[main] pid : {cp.pid}')
    print("[main] end")

# if __name__ == "__main__" 사용하는 이유 
# https://docs.python.org/2/library/multiprocessing.html#multiprocessing-programming