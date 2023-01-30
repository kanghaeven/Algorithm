# 큐 # 선입선출

import sys
n = int(input())
queue = []

for i in range(n):
    user = sys.stdin.readline().split()

    if user[0] == 'push':
        queue.append(user[1])

    if user[0] == 'pop': # 큐에서 가장 앞에 있는 정수를 빼
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    
    if user[0] == 'size':
        print(len(queue))
    
    if user[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    if user[0] == 'front': # 큐의 가장 앞에 있는 정수
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    if user[0] == 'back': # 큐의 가장 뒤에 있는 정수
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])