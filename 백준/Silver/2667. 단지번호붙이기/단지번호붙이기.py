import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, *input().split())) for _ in range(N)]

di = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def dfs(x, y):
    size = 1
    arr[x][y] = 0
    for f in range(4):
        nx, ny = x + di[f][0], y + di[f][1]
        if nx >= 0 and ny >= 0 and nx < N and ny < N:
            if arr[nx][ny] != 0:
                size += dfs(nx, ny)
    return size

cnt = 0
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            ans.append(dfs(i, j))
            cnt += 1

print(cnt)
if ans:
    ans.sort()
    for a in ans:
        print(a, end ='\n')