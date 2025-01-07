import sys
input = sys.stdin.readline

N = int(input())
[A, B] = list(map(int, input().split(' ')))
M = int(input())

ans = []
graph = [[] for _ in range(N + 1)]

for i in range(M):
    [a, b] = list(map(int, input().split(' ')))
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, end):
    global cnt, ans
    if start == end:
        visited[start] = 2
        ans.append(cnt)
        return
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i, end)
            cnt -= 1

cnt = 0
visited = [0 for _ in range(N + 1)]
dfs(A, B)
cnt = 0
visited = [0 for _ in range(N + 1)]
dfs(B, A)

if 2 in visited:
    print(min(ans))
else:
    print(-1)
