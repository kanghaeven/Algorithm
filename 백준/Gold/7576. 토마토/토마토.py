dx = [0,1,0,-1]
dy = [1,0,-1,0]

from collections import deque
def bfs(one): # 익은 토마토(들) (동시에) 탐색
    level = 0 # 날짜
    queue = deque()
    for j in one:
        queue.append([j[0], j[1], level]) # 각각 익은 토마토 탐색 위해 추가
        visited[j[0]][j[1]] = True # 방문 처리

    while queue:
        ripe = queue.popleft() # 탐색 대상
        level = ripe[2] # 날짜 업데이트
        for i in range(4): # 사방 탐색
            nx = ripe[0] + dx[i]
            ny = ripe[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0: # 안 익었으면 익혀
                    box[nx][ny] = 1
                    visited[nx][ny] = True
                    # 그대로 cnt 넣으면 4번 카운트됨
                    queue.append([nx, ny, level + 1]) # 다음 탐색 대상과 날짜 카운트
    return level # 날짜 반환

M, N = map(int, input().split()) # M 가로칸 수, N 세로칸 수 
box = [list(map(int, input().split())) for _ in range(N)] # 토마토 상태
visited = [[False for _ in range(M)] for _ in range(N)] # 방문 처리
flag = True

one = [] # 익은 토마토 리스트
for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            one.append([x, y])
            
result = bfs(one) # 최소 날짜 구하기

for xx in range(N):
    for yy in range(M):
        if box[xx][yy] == 0: # 탐색한 후에도 모두 익지 못하는 상황
            flag = False 

if flag == True:
    print(result)
else:
    print(-1)
