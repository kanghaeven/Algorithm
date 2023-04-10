import heapq
import sys
input = sys.stdin.readline

V = int(input()) # 정점
E = int(input()) # 간선

distance = [int(1e9) for _ in range(V+1)] # 최단 거리 테이블 무한대로 초기화
graph = [[] for _ in range(V+1)] # 노드 정보 받을 리스트

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

S, E = map(int, input().split()) # 시작점 도착점
def dijkstra(S):
    pq = [(0, S)] # 가중치, 시작 정점
    distance[S] = 0 # 최단 거리 테이블 시작 정점 = 0 처리

    while pq:
        w, u = heapq.heappop(pq)
        if u == E: # 도착정점이면 종료
            return distance[E] # 최단거리 테이블에서 도착정점에 저장된 최소비용 반환

        if distance[u] < w: # 이미 처리된 노드라면 넘어감
            continue

        for v, tw in graph[u]: # 인접 정점, 가중치
            nw = distance[u] + tw # 새 가중치 = 탐색 노드까지의 거리 + 인접 가중치
            if nw < distance[v]: # 새 가중치 < 인접 노드까지의 거리면
                distance[v] = nw # 인접 노드까지의 거리 = 새 가중치로 갱신
                heapq.heappush(pq, (distance[v], v)) # (새 가중치, 인접 노드) 경로로 탐색하기 위해 넣기

    return distance

print(dijkstra(S))
