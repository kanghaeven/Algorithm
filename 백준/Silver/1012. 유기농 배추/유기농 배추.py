import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

di = [[0, -1], [-1, 0], [0, 1], [1, 0]]

def dfs(a, b):
    ground[a][b] = -1
    for f in range(4):
        [nx, ny] =  a + di[f][0], b + di[f][1]
        if nx >= 0 and ny >= 0 and nx < N and ny < M and ground[nx][ny] == 1:
            dfs(nx, ny)
    return

T = int(input())
for _ in range(T):
    cnt = 0
    [M, N, K] = list(map(int, input().split(' ')))
    ground = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        [X, Y] = list(map(int, input().split(' ')))
        ground[Y][X] = 1
    
    for n in range(N):
        for m in range(M):
            if ground[n][m] == 1:
                dfs(n, m)
                cnt += 1
    
    print(cnt)

