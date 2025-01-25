from pprint import pprint

from collections import deque
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split(' ')))
arr = [list(map(int, input().strip())) for _ in range(N)]
di = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs():
    q = deque([(0, 0, 0)]) # x, y, wall 0은 안뿌셔 1은 뿌셔
    visited = [[[-1, -1] for _ in range(M)] for _ in range(N)] # [안뿌신 최소거리, 뿌신 최소거리]
    visited[0][0][0] = 1 # 시작은 안뿌신 거리 1
    
    while q:
        x, y, wall = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][wall]

        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0 and visited[nx][ny][wall] == -1: # 이동 가능하고, 현재 벽 상태에서 미방문이면
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))
                elif arr[nx][ny] == 1 and wall == 0 and visited[nx][ny][1] == -1: # 다음칸이 벽이고, 아직 벽 부순 적 없고, 미방문이면
                    visited[nx][ny][1] = visited[x][y][wall] + 1
                    q.append((nx, ny, 1))
    return -1

print(bfs())