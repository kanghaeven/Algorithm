from collections import deque
import sys
input = sys.stdin.readline

[N, M, K, X] = list(map(int, input().strip().split(' ')))

city = [[] for _ in range(N + 1)]
ans = []

for _ in range(M):
    [a, b] = list(map(int, input().strip().split(' ')))
    city[a].append(b)

def bfs(start):
    visited = [-1 for _ in range(N + 1)]
    q = deque([])
    q.append(start)
    visited[start] = 0
    while q:
        node = q.popleft()
        for c in city[node]:
            if visited[c] == -1:
                visited[c] = visited[node] + 1
                q.append(c)
    return visited

result = bfs(X)

for i in range(1, N + 1):
    if result[i] == K:
        ans.append(i)

if ans:
    ans.sort()
    print(*ans, sep='\n')
else:
    print(-1)