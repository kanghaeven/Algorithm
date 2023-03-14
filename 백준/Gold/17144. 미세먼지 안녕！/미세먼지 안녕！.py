import sys
input = sys.stdin.readline
R, C, T = map(int, input().split()) # 세로 # 가로
A = [list(map(int, input().split())) for _ in range(R)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for t in range(T): # 초마다 순회

    # 미세먼지 확산
    dust = []
    for r in range(R): # 미세먼지가 있는 모든 칸 구하기
        for c in range(C):
            if A[r][c] > 0:
                dust.append([r, c])

    # 미세먼지 있는 칸만 확산
    for d in dust:
        spread = 0
        x = d[0]
        y = d[1]
        for i in range(4): # 인접한 네 방향으로 확산 
            nx = x + dx[i] 
            ny = y + dy[i] 
            if 0 <= nx < R and 0 <= ny < C: # 칸이 있고 
                if A[nx][ny] != -1: # 공기청정기 아니면 
                    d.append([nx,ny]) # 확산 
                    d.append(A[x][y] // 5) # 확산 
                    spread += 1 
        d.append(spread)
        A[x][y] -= (A[x][y] // 5) * spread # Ar,c - (Ar,c/5)×(확산된 방향의 개수)

    # print(dust) # dust[0] = [0, 7, [1, 7], 1, [0, 6], 1, 2]
    for d in dust:
        for n in range(d[-1]):
            xx = d[(n + 1) * 2][0]
            yy = d[(n + 1) * 2][1]
            A[xx][yy] += d[((n + 1) * 2) + 1]
    # pprint(A) # 확산 완료

    # 공기청정기 작동
    # 공기청정기 A[2:R-1][0] == -1
    clean = []
    for a in range(2, R-1):
        if A[a][0] == -1:
            clean.append(a)

    # 위쪽 반시계 방향 이동
    up01 = A[clean[0]][1:C-1]
    up01.insert(0,0) # [0, 2, 1, 1, 0, 4, 6] 

    up02 = [] # [6, 5]
    for u in range(1, clean[0]+1):
        up02.append(A[u][-1])

    up03 = A[0][1:C] # [0, 0, 0, 0, 0, 1, 8]

    up04 = [] # [0]
    for u in range(clean[0]-1):
        up04.append(A[u][0])

    A[clean[0]][1:C] = up01 # A[2][1:8]

    for u in range(clean[0]): #A[0:clean[0]]
        A[u][-1] = up02[u]

    A[0][0:C-1] = up03 # A[0][0:7]

    for u in range(clean[0]-1): # A[1:clean[0]]
        A[u+1][0] = up04[u]


    # 아래쪽 시계 방향 이동
    down01 = A[clean[1]][1:C-1]
    down01.insert(0,0) # [0, 5, 2, 0, 0, 2, 12]

    down02 = [] # [0, 8, 0]
    for u in range(clean[1], R-1):
        down02.append(A[u][-1])

    down03 = A[-1][1:C] # [8, 17, 8, 3, 4, 8, 4]

    down04 = [] # [0, 0]
    for u in range(clean[1]+2, R):
        down04.append(A[u][0])

    A[clean[1]][1:C] = down01 # A[3][1:8]

    for u in range(clean[1]+1, R): # A[4:7][-1]
        A[u][-1] = down02[u-(clean[1]+1)]

    A[-1][0:C-1] = down03 # A[-1][0:7]

    for u in range(clean[1]+1, R-1): # A[4:6][0]
        A[u][0] = down04[u-(clean[1]+1)]

sum = 0
for du in range(R):
    for st in range(C):
        if A[du][st] > 0:
            sum += A[du][st]

print(sum) # 순회가 끝난 뒤 남은 미세먼지 합