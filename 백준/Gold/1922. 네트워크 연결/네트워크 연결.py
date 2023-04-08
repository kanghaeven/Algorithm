import sys
import heapq
input = sys.stdin.readline
V = int(input()) # 컴퓨터 정점
E = int(input()) # 연결 간선
graph = [set() for _ in range(V + 1)]

for _ in range(E):
    u, v, cost = map(int, input().split()) # 시작 정점, 도착 정점, 비용
    graph[u].add((v, cost))
    graph[v].add((u, cost))
    
def prim(graph):
    pq = [(0, 1)] # 가중치, 임의의 시작 정점
    ans = 0 # 최소 비용
    visited = [False for _ in range(V + 1)]
    
    while pq:
        cost, u = heapq.heappop(pq) # 가중치, 탐색 정점
        if visited[u]: # 방문했으면
            continue # 건너뜀
        visited[u] = True # 방문 안 했으면 방문 처리
        ans += cost # 비용 추가
        
        for v, cost in graph[u]: # 탐색 정점에 연결되어 있는 모든 정점 살펴봄
            if visited[v] == False: # 방문 안 했으면
                # 비용을 먼저 넣어 우선순위 큐에서 비용을 기준으로 오름차순 정렬
                heapq.heappush(pq, (cost, v))
    
    return ans

print(prim(graph))