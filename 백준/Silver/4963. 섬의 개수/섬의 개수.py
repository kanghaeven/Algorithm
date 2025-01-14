import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

di = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
flag = 1

def dfs(x, y):
    arr[x][y] = 2
    for e in range(8):
        nx, ny = x + di[e][0], y + di[e][1]
        if nx >= 0 and ny >= 0 and nx < h and ny < w and arr[nx][ny] == 1:
            dfs(nx, ny)
    return

while flag:
    [w, h] = list(map(int, input().strip().split(' ')))
    if [w, h] == [0, 0]:
        flag = 0
        break
    cnt = 0
    arr = [list(map(int, input().strip().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)