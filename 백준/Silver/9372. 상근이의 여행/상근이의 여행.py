# 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수 
# 인덱스 1, 2, 3 출발지 [도,착,지] 각 국가에 가는 비행기 그래프
# 나라 == 정점
# 비행기 == 간선

def dfs(v): # dfs 탐색 # dfs, bfs 어떤 탐색 쓰든 상관은 없음
    global cnt
    stack = [] # 후입선출 스택 (가장 깊은 정점 먼저 뽑기)
    visited[v] = True
    # print(v, end ='')
    for i in airplane[v]:
        if visited[i] == False:
            cnt += 1
            stack.append(i)
            dfs(stack.pop())


import sys
T = int(sys.stdin.readline()) 

for tc in range(T):
    N, M = map(int, sys.stdin.readline().split()) # N 국가 수, M 비행기 종류
    airplane = [list() for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    cnt = 0
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split()) # a와 b를 왕복하는 비행기
        airplane[a].append(b)
        airplane[b].append(a)
    # print(airplane) # [[], [2, 3], [1, 3], [2, 1]]
    dfs(1)
    print(cnt)


