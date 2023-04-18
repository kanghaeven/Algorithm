
# 노드의 개수와 간선의 개수를 입력 받기
V, E = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (V + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(V + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b) # a 먼저 풀고 b 풀기
    # 진입 차수를 1 증가
    indegree[b] += 1
# print(graph) 
    
# 위상 정렬 함수
def topology_sort():
    result = []
    lst = []

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, V + 1):
        if indegree[i] == 0:
            lst.append(i)

    # 리스트가 빌 때까지 반복
    while lst:
        lst.sort()
        # 리스트에서 원소 꺼내기
        now = lst.pop(0)
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                lst.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')
        
topology_sort()