from collections import deque

def bfs(v): # bfs 탐색
    visited = [False for _ in range(N + 1)]
    ans = [0 for _ in range(N + 1)]

    queue = deque()
    queue.append(v)
    visited[v] = True # 루트 노드 방문 처리

    while queue:
        node = queue.popleft()

        for nxt_node in tree[node]:
            if visited[nxt_node] == False:
                queue.append(nxt_node)
                visited[nxt_node] = True
                ans[nxt_node] = node

    print(*ans[2:], sep = '\n')

N = int(input())
num = [list(map(int, input().split())) for _ in range(N-1)]
tree = [[] for _ in range(N+1)]
for i in range(N-1):
    tree[num[i][0]].append(num[i][1])
    tree[num[i][1]].append(num[i][0])
# print(tree) # [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

bfs(1)