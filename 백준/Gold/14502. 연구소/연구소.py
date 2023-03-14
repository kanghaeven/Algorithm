
import sys
input = sys.stdin.readline
from collections import deque 

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)] # 0 빈칸 1 벽 2 바이러스
# pprint(area)

# 새로 세울 벽 개수 3개
# 0을 세울 수 있는 3 좌표 경우의 수 -> 벽 세우고 -> 0이 이어져 있는 애들 탐색 -> 개수 카운트
zero = []
for x in range(N):
    for y in range(M):
        if area[x][y] == 0:
            zero.append([x,y])
# print(zero)

from itertools import combinations
a = list(combinations(zero, 3))

for i in range(len(a)): # 튜플 리스트 변환
    a[i] = list(a[i])
# print(a[0]) # [[0, 1], [0, 2], [0, 3]]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

mx = []

for i in range(len(a)): # 구한 경우의 수만큼 순회

    for j in range(3): # 각 경우의 수의 길이는 3
        area[a[i][j][0]][a[i][j][1]] = 1 # 벽 세우기

    each = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for xx in range(N): # 크기만큼 돌려 0 찾기
        for yy in range(M):
            szero = 0
            if area[xx][yy] == 0 and visited[xx][yy] == 0: 
                
                szero = 1
                visited[xx][yy] = 1
                queue = deque()
                queue.append([xx, yy])

                flag = True
                while queue:
                    ii, jj = queue.popleft()
                    for f in range(4): # 사방 탐색 
                        nx = ii + dx[f]
                        ny = jj + dy[f]
                        if 0 <= nx < N and 0 <= ny < M: 
                            if area[nx][ny] == 0 and visited[nx][ny] == 0: # 사방탐색 중 0이면 
                                szero += 1
                                visited[nx][ny] = 1
                                queue.append([nx, ny])

                            if area[nx][ny] == 2:
                                flag = False                                

                if flag == False:
                    szero = 0

            each += szero

    mx.append(each)
    
    for j in range(3): # 벽 세운 거 0으로 바꾸기
        area[a[i][j][0]][a[i][j][1]] = 0 

print(max(mx))
