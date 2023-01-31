import sys
from collections import deque #deque 자료구조 사용하기 위해 다음과 같이 선언

n, m = map(int,sys.stdin.readline().split()) # n은 큐의 크기, m은 뽑을 개수
que = deque([i for i in range(1, n+1)]) # 큐 생성
idx = list(map(int,sys.stdin.readline().split())) # 뽑아내려고 하는 원소의 위치

cnt = 0 # 2,3번 수행 시 카운트

for i in idx: # 뽑아내려고 하는 원소의 위치 for문으로 순회

    while True: # 뽑을 때까지 순회

        if que[0] == i: # 큐의 첫 인덱스가 뽑아내려고 하는 원소의 위치와 같으면
            que.popleft() # 1번 수행
            break # 그만
        else: 
            if que.index(i) <= len(que) // 2: # mid 값 보다 i인덱스 위치가 작으면 왼쪽
                que.rotate(-1) # 음수는 왼쪽 회전 # 2번 수행
                cnt += 1
            else:
                que.rotate(1) # 양수는 오른쪽 회전 # 3번 수행
                cnt += 1
print(cnt)
