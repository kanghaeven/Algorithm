import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

[N, M, K] = list(map(int, input().strip().split(' ')))

friendcost = list(map(int, input().strip().split(' ')))

friend = [set() for _ in range(N)]

for _ in range(M):
    [v, w] = list(map(int, input().strip().split(' ')))
    if v != w:
        friend[v - 1].add(w - 1)
        friend[w - 1].add(v - 1)

visited = [0 for _ in range(N)]
cost = 0

def dfs(node, group):
    visited[node] = 1
    group.append(node)
    # print(node, visited, friendcost[node])
    for f in friend[node]:
        if visited[f] == 0:
            dfs(f, group)

for i in range(N):
    if visited[i] == 0:
        group = []
        dfs(i, group)
        # print(group)
        cost += min(friendcost[j] for j in group)
        if cost > K:  
            break

if cost <= K:
    print(cost)
else:
    print('Oh no')