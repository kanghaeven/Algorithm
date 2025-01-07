import sys
input = sys.stdin.readline

[N, M, V] = list(map(int, input().split(' ')))

arr = [list(map(int, input().strip().split(' '))) for _ in range(M)]

graph = [[] for _ in range(N + 1)]

for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for g in graph:
    g.sort()

def dfs(node):
    visited[node] = 1
    for n in graph[node]:
        if visited[n] == 0:
            ansd.append(n)
            dfs(n)
    return ansd

from collections import deque
q = deque()

def bfs(node):
    q.append(node)
    while q:
        n = q.popleft()
        if visited[n] == 0:
            ansb.append(n)
            visited[n] = 1
        for g in graph[n]:
            if visited[g] == 0:
                q.append(g)
    return ansb

visited = [0 for _ in range(N + 1)]
ansd = [V]
print(*dfs(V))

visited = [0 for _ in range(N + 1)]
ansb = []
print(*bfs(V))