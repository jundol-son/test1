# 텍스트 파일이 반드시 존재해야 함.
with open("2일차/write.txt", "w") as f:
    f.write('Hi\n')    
    f.write('Hello')    

with open("2일차/write.txt", "w") as f:
    f.writelines(['Hi\n', 'Hello'])