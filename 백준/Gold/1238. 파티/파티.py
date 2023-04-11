
import heapq
import sys
input = sys.stdin.readline
V, E, X = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다 
def dijkstra(start, end):
    pq = [(0, start)] # 가중치, 시작 정점 
    distance = [int(1e9) for _ in range(V + 1)] # 각 학생마다 최단 시간 구하기 위해 거리 초기화
    distance[start] = 0 # 시작 정점 처리
    
    while pq:
        w, u = heapq.heappop(pq)
        if u == end:
            return distance[end]
        
        if distance[u] < w: # 이미 처리한 노드면 넘어감
            continue
        
        for v, tw in graph[u]: # 인접한 노드들 탐색
            nw = distance[u] + tw # 새 가중치 = 탐색 노드까지의 거리 + 인접 노드의 가중치
            if nw < distance[v]: # 새 가중치가 인접 노드까지의 거리보다 작으면
                distance[v] = nw # 인접 노드 까지의 거리 = 새 가중치
                heapq.heappush(pq, (distance[v], v)) 
    return distance

mx = 0
for i in range(1, V + 1):
    if i == X:
        continue
    go = dijkstra(i, X) # 학생마다 집에서 파티장소까지 가는 최단 거리
    back = dijkstra(X, i) # 학생마다 파티장소에서 집까지 오는 최단 거리
    student = go + back
    if mx < student:
        mx = student
        
print(mx) # 장 많은 시간을 소비하는 학생의 소요시간