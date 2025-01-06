import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

[N, M] = map(int, input().split(' '))

graph = [list(map(int, input().split(' '))) for _ in range(M)]

arr = [[] for _ in range(N)]

visited = [0 for _ in range(N)]


def dfs(node):
    visited[node] = 1
    for k in arr[node]:
        if visited[k] == 0:
            dfs(k)      
    return

for a, b in graph:
    arr[a - 1].append(b - 1)
    arr[b - 1].append(a - 1)    

cnt = 0

for i in range(N):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
