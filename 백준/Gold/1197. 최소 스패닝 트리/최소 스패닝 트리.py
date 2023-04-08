def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b  


V, E = map(int, input().split())
# 부모 테이블 초기화 
parent = [0] * (V + 1)
# 부모 테이블 상에서 부모 자기 자신으로 초기화
for i in range(1, V + 1):
    parent[i] = i
    
edges = [] # 모든 간선 담을 리스트
result = 0 # 최소 비용 담을 변수

for e in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)