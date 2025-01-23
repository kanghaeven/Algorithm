import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

[N, M] = list(map(int, input().strip().split(' ')))
arr = [[*input().strip()] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
di = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def dfs(x, y, group_num):
    visited[x][y] = group_num 
    nx, ny = x + di[arr[x][y]][0], y + di[arr[x][y]][1]

    if 0 <= nx < N and 0 <= ny < M:
        if visited[nx][ny] == 0:  # 미방문 상태라면
            return dfs(nx, ny, group_num)  # 재귀 호출
        elif visited[nx][ny] == group_num:  # 싸이클 발견
            return True
    return False  # 다른 조건에서는 False 반환

cnt = 0
group_num = 1
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            if dfs(i, j, group_num):
                cnt += 1
            group_num += 1  # 새로운 그룹 번호 증가

print(cnt)
