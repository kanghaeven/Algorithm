from collections import deque
import sys
input = sys.stdin.readline

[M, N] = list(map(int, input().strip().split(' ')))
box = [list(map(int, input().strip().split(' '))) for _ in range(N)]

di = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def bfs(tomato):
    q = deque([tomato])
    for t in tomato:
        box[t[0]][t[1]] = 1
    cnt = -1

    while q:        
        arr = q.popleft()

        if not arr:
            break
        
        cnt += 1
        for a in arr:
            box[a[0]][a[1]] = 1

        tmp = []
        for a in arr:
            for f in range(4):
                nx, ny = a[0] + di[f][0], a[1] + di[f][1]
                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    box[nx][ny] = 1
                    tmp.append((nx, ny))
        q.append(tmp)

    for n in box:
        if 0 in n:  
            return -1
    return cnt

    # checkzero = []
    # for aa in range(N):
    #     for bb in range(M):
    #         if box[aa][bb] == 0:
    #             checkzero.append([aa, bb])

    # for check in checkzero:
    #     for ff in range(4):
    #         cx, cy = check[0] + di[ff][0], check[1] + di[ff][1]
    #         if 0 <= cx < N and 0 <= cy < M and box[cx][cy] <= 0:
    #             cnt = -1
    
    # return cnt

tomato = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i, j))

print(bfs(tomato))
        