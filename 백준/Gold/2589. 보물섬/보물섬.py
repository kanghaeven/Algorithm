from collections import deque
import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().strip().split(' ')))

arr = [[*input().strip()] for _ in range(N)]
di = [[0, -1], [0, 1], [1, 0], [-1, 0]]

def bfs(x, y):
    q = deque([])
    q.append([x, y])
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[i][j] = 0
    maxcnt = 0
    while q:
        sx, sy = q.popleft()
        for dx, dy in di:
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 'L' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[sx][sy] + 1
                maxcnt = max(maxcnt, visited[nx][ny])
                q.append([nx, ny])
    return maxcnt

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            ans = max(ans, bfs(i, j))

print(ans)