from collections import deque
import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split(' ')))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    [a, b] = list(map(int, input().split((' '))))
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, end):
    q = deque([])
    visited = [0 for _ in range(N + 1)]
    q.append(start)
    visited[start] = 1
    while q:
        current = q.popleft()

        if current == end:
            return visited[end] - 1
        
        for n in graph[current]:
            if visited[n] == 0:
                visited[n] = visited[current] + 1
                q.append(n)
    return

ans = []
for i in range(1, N + 1):
    arr = [j for j in range(1, N + 1)]
    node = arr.pop(i - 1)
    cnt = 0
    for a in arr:
        cnt += bfs(node, a)
    ans.append(cnt) 

print(ans.index(min(ans)) + 1)