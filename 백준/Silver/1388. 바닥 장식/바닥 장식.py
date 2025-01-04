import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split(' ')))

room = [[*input().strip()] for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]

garo = [[0, -1], [0, 1]]
sero = [[-1, 0], [1, 0]]

def row(x, y):
    visited[x][y] = 1
    for g in range(2):
        ny = y + garo[g][1]
        if ny >= 0 and ny < M and visited[x][ny] == 0 and room[x][ny] == '-':
            row(x, ny)
    return

def col(x, y):
    visited[x][y] = 1
    for s in range(2):
        nx = x + sero[s][0]
        if nx >= 0 and nx < N and visited[nx][y] == 0 and room[nx][y] == '|':
            col(nx, y)
    return

cnt = 0

for i in range(N):
    for j in range(M):
        if room[i][j] == '-' and visited[i][j] == 0:
            row(i, j)
            cnt += 1

for i in range(M):
    for j in range(N):
        if room[j][i] == '|' and visited[j][i] == 0:
            col(j, i)
            cnt += 1
            
print(cnt)