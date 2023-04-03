def dfs(n, v): # 중복없이 빠짐없이
    if n == 5:
        return True

    for w in adjL[v]:   # v와 인접하고
        if visited[w] == 0:   # 방문한적이 없는 w가 있으면
            visited[w] = 1    # 방문 처리
            x = dfs(n + 1, w)    # 방문
            if x :
                return True
            visited[w] = 0    # 원상 복구

# 4 1 0 3 2
# 0 1 2 3 
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
