import heapq
import sys
input = sys.stdin.readline

M, N = map(int, input().strip().split(' '))

maze = [list(map(int, input().strip())) for _ in range(N)]

di = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def dijkstra():
    heap = [(0, 0, 0)]
    distance[0][0] = 0

    while heap:
        d, x, y = heapq.heappop(heap)
        
        if x == N-1 and y == M-1:
            return distance[N-1][M-1]
        
        if distance[x][y] < d:
            continue

        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if distance[nx][ny] == 1e9:
                    nd = d
                    if maze[nx][ny] == 1:
                        nd += 1
                    distance[nx][ny] = nd
                    heapq.heappush(heap, (nd, nx, ny))

distance = [[1e9 for _ in range(M)] for _ in range(N)]

print(dijkstra())