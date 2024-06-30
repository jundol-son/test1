# 텍스트 파일이 반드시 존재해야 함.
with open("2일차/read.txt") as f:
    data = f.readlines()
    for line in data:
        print(line.strip())

with open("2일차/read.txt") as f:
    for line in f:
        print(line.strip())
