from collections import deque
import sys
input = sys.stdin.readline

di = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(rupee):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = rupee[0][0]

    while q:
        sx, sy = q.popleft()
        for dx, dy in di:
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < N and 0 <= ny < N:
                newcost = visited[sx][sy] + rupee[nx][ny]       
                if visited[nx][ny] == -1 or newcost < visited[nx][ny]:
                    visited[nx][ny] = newcost
                    q.append([nx, ny])
   
    return visited[N-1][N-1]

i = 0
while True:
    N = int(input())
    if N == 0:
        break

    rupee = [list(map(int, input().strip().split(' '))) for _ in range(N)]

    i += 1
    print(f"Problem {i}: {bfs(rupee)}")