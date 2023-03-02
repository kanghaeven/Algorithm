dx = [0,1,0,-1]
dy = [1,0,-1,0]

from collections import deque
def bfs(one): # list에 토마토가있어
    global flag
    level = 0
    queue = deque()
    for j in one:
        queue.append([j[0], j[1], level]) # append 할 때 토마토를 넣어주면 되겠지..?
        visited[j[0]][j[1]] = True

########################################## 레벨은 어디다가 넣어야 할까요...?
    while queue:
        ripe = queue.popleft() 
        level = ripe[2]
        for i in range(4):
            nx = ripe[0] + dx[i]
            ny = ripe[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0:
                    box[nx][ny] = 1
                    visited[nx][ny] = True
                    queue.append([nx, ny, level + 1]) # ...? = Node == level = ?

    return level

M, N = map(int, input().split()) # M 가로칸 수, N 세로칸 수 
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
flag = True

one = []
for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            one.append([x, y])
            
result = bfs(one)

for xx in range(N):
    for yy in range(M):
        if box[xx][yy] == 0:
            flag = False 

if flag == True:
    print(result)
elif flag == False:
    print(-1)
