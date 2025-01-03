nodes = int(input())
edges = int(input())
graph = [[] for _ in range(nodes + 1)]
visited = [0 for _ in range(nodes + 1)]

for c in range(edges):
    tmp = list(map(int, input().split()))
    graph[tmp[0]] += [tmp[1]]
    graph[tmp[1]] += [tmp[0]]

# print(graph)

def dfs(start):
    visited[start] = 1
    for n in graph[start]:
        # print("바이러스", n)
        # print(visited)
        if visited[n] == 0:
            dfs(n)
    return sum(visited)

print(dfs(1) - 1)