
import heapq
import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

distance = [int(1e9) for _ in range(V+1)]
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

S, E = map(int, input().split())

def dijkstra(S):
    pq = [(0, S)]
    distance[S] = 0

    while pq:
        w, u = heapq.heappop(pq)
        if u == E:
            return distance[E]

        if distance[u] < w: # 이미 처리된 노드라면 넘어감
            continue

        for v, tw in graph[u]: # 인접 정점, 가중치
            nw = distance[u] + tw # 새 가중치 = 탐색 노드까지의 거리 + 인접 가중치
            if nw < distance[v]: # 새 가중치 < 인접 노드까지의 거리면
                distance[v] = nw # 인접 노드까지의 거리 = 새 가중치로 갱신
                heapq.heappush(pq, (distance[v], v)) # (새 가중치, 인접 노드) 경로로 탐색하기 위해 넣기

    return distance

print(dijkstra(S))
