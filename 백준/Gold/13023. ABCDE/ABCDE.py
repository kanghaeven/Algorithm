
import sys
def dfs(n, v): # 중복없이 빠짐없이
    if n == 5:
        print(1) 
        sys.exit() # 시스템 종료
        # return True

    for w in adjL[v]:   # v와 인접하고
        if visited[w] == 0:   # 방문한적이 없는 w가 있으면
            visited[w] = 1    # 방문 처리
            x = dfs(n + 1, w)    # 방문
            # if x : # 재귀가 끝까지 돌기때문에 
            #     return True # 참으로 종료 
            visited[w] = 0    # 원상 복구


N, M = map(int, input().split())
adjL = [set() for _ in range(N+1)] # 중복없애기
visited = [0 for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    adjL[a].add(b)
    adjL[b].add(a)


for i in range(N):
    visited[i] = 1 # 시작 노드 방문 처리
    dfs(1, i)
    visited[i] = 0 # 원상 복구

print(0) # 시스템 종료 안되면 for문 다돌고 0 출력





'''def dfs(n, v): # 중복없이 빠짐없이
    if n == 5:
        return True

    for w in adjL[v]:   # v와 인접하고
        if visited[w] == 0:   # 방문한적이 없는 w가 있으면
            visited[w] = 1    # 방문 처리
            x = dfs(n + 1, w)    # 방문
            if x : # 재귀가 끝까지 돌기때문에 
                return True # 
            visited[w] = 0    # 원상 복구


N, M = map(int, input().split())
adjL = [set() for _ in range(N+1)] # 중복없애기
visited = [0 for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    adjL[a].add(b)
    adjL[b].add(a)


for i in range(N):
    visited[i] = 1 # 시작 노드 방문 처리
    if dfs(1, i):
        print(1)
        break
    visited[i] = 0 # 원상 복구
else:
    print(0)
'''