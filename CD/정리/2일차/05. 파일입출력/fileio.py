# with open('read.txt', encoding='utf-8') as f:
#     data = f.readlines()
#     print(data)

with open('read.txt', 'w') as f:
    # f.write('출력-1\n')
    # f.write('출력-2\n')
    f.writelines(['라인-1\n','라인-2\n'])
    
with open('read.txt', 'a') as f:
    # f.write('출력-1\n')
    # f.write('출력-2\n')
    f.write('출력을 추가했어요.\n')

outputs = []
outputs.append('출력\n')

outputs.append('추ㅜㄹ력 추가했어요 리스트로\n')
with open('write.txt', 'w') as f:
    f. writelines(outputs)