N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 연결되어있는 외부공기 처리 2

def outside(): # 외부공기 처리할 시작점 찾는 함수
    for n in range(N):
        for m in range(M):
            if paper[n][m] == 0:
                bfs(n, m) # 외부공기 처리 함수
                return
            

from collections import deque
def bfs(n, m):
    
    queue = deque()
    queue.append([n, m]) # 첫 탐색 좌표 넣기
    paper[n][m] = 2

    while queue:
        out = queue.popleft()
        for i in range(4):
            nx = out[0] + dx[i]
            ny = out[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if paper[nx][ny] == 0:
                    paper[nx][ny] = 2
                    queue.append([nx, ny])

outside()


def disapper(n, m): # 치즈 녹이는 함수

    air = 0 # 공기와 접촉하는 변 카운트
    for i in range(4): 
        nx = n + dx[i]
        ny = m + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if paper[nx][ny] == 2:
                air += 1
    
    if air >= 2: # 2변 이상 접촉하면 녹음
        melt.append([n,m]) # 동시에 녹는 것 고려
    return melt


cnt = 0
while True: 
    cnt += 1 # 시간 카운트
    melt = []
    for x in range(N):
        for y in range(M):
            if paper[x][y] == 1: # 치즈 녹이기
                disapper(x, y)

    for i, j in melt: # 동시에 녹음
        paper[i][j] = 2
        bfs(i,j)


    two = 0 # 전부 다 녹았을 때 반복 멈춰
    for x in range(N):
        for y in range(M):
            if paper[x][y] == 2:
                two += 1
    if two == N * M:
        break

# pprint(paper)
print(cnt) # 치즈가 모두 녹아 없어지는데 걸리는 시간
