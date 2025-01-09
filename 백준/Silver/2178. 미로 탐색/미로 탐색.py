from collections import deque
import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split(' ')))

arr = [list(map(int, *input().strip().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]

q = deque([])

def bfs(x, y):
    q.append([x, y])
    visited[x][y] = 1

    while q:
        [a, b] = q.popleft()
        if a == N - 1 and b == M - 1:
            return visited[a][b]
        for f in range(4):
            nx, ny = a + di[f][0], b + di[f][1]
            if nx >= 0 and ny >= 0 and nx < N and ny < M and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[a][b] + 1
                q.append([nx, ny])
    return

print(bfs(0, 0))