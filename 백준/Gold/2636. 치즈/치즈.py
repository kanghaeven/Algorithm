from collections import deque
import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().strip().split(' ')))

arr = [list(map(int, input().strip().split(' '))) for _ in range(N)]

di = [[0, 1], [1, 0], [0, -1], [-1, 0]]

ans = []

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    cnt = 0
    # 한번 while문 반복할 때마다 1시간 지남
    while q:
        x, y = q.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if arr[nx][ny] == 0:
                    # 가장자리만 체크하기 위해 치즈가 아닌 공기만 q에 넣음
                    q.append((nx,ny))
                elif arr[nx][ny] == 1:
                    # 넣게되면 안쪽 치즈까지 녹기 때문에 공기와 접촉한 치즈는 q에 넣지 않음
                    arr[nx][ny] = 0
                    cnt += 1
    ans.append(cnt)
    return cnt

time = 0
while True:
    time += 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    if bfs() == 0:
        break

print(time - 1)
print(ans[-2])