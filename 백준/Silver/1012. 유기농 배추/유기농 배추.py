import sys
sys.setrecursionlimit(10000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if area[nx][ny] == 1:
                area[nx][ny] = 0
                dfs(nx, ny)

T = int(input())
for tc in range(T):
    M, N, K = map(int,input().split())
    area = [[0 for _ in range(N)] for _ in range(M)]
    cnt = 0

    for k in range(K):
        x, y = map(int, input().split())
        area[x][y] = 1
    # pprint(area)

    for x in range(M):
        for y in range(N):
            if area[x][y] == 1:
                dfs(x,y)
                cnt += 1  

    print(cnt)