from collections import deque
import sys
input = sys.stdin.readline

[N, K] = list(map(int, input().strip().split(' ')))
visited = [0 for _ in range(100001)]
q = deque([N])
visited[N] = 1

def bfs():
    while q:
        n = q.popleft()

        if n == K:
            return visited[K] - 1

        for i in [n - 1, n + 1, n * 2]:
            if 0 <= i <= 100000 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[n] + 1

print(bfs())