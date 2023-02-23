
import sys
input = sys.stdin.readline
t1 = list(input().rstrip()) # str으로 입력을 받아 개행문자 제거
M = int(input())
t2 = [] # 두 개의 리스트로 간격을 내겠다
# 커서의 위치
for m in range(M):
    cmd = list(input().split())

    if cmd[0] == 'L': # 커서를 왼쪽으로 한 칸 옮김 
        if t1:
            t2.append(t1.pop())

    if cmd[0] == 'D': # 커서를 오른쪽으로 한 칸 옮김
        if t2:
            t1.append(t2.pop()) 
    
    if cmd[0] == 'B': # 커서 왼쪽에 있는 문자를 삭제함 
        if t1:
            t1.pop() 

    if cmd[0] == 'P': # $라는 문자를 커서 왼쪽에 추가함
        t1.append(cmd[1]) 

t1.extend(reversed(t2)) # t1[안, 녕] t2[요, 세, 하]
print(''.join(t1))
