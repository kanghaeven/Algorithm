import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

[M, N, K] = list(map(int, input().strip().split()))

arr = [[0 for _ in range(N)] for _ in range(M)]
di = [[0, 1], [-1, 0], [1, 0], [0, -1]]
cnt = 0
ans = []

def dfs(a, b):
    global size
    arr[a][b] = -1
    size += 1
    for f in range(4):
        nx, ny = a + di[f][0], b + di[f][1]
        if nx >= 0 and ny >= 0 and nx < M and ny < N and arr[nx][ny] == 0:
            dfs(nx, ny)        

for _ in range(K):
    [sx, sy, ex, ey] = list(map(int, input().strip().split()))
    for x in range(sy, ey):
        for y in range(sx, ex):
            arr[x][y] = 1

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            size = 0
            dfs(i, j)
            cnt += 1
            ans.append(size)

print(cnt)
ans.sort()
print(*ans)