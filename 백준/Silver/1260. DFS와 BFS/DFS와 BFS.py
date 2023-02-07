N, M, V = map(int,input().split()) # N 정점 수, M 간선 수, V 탐색 시작 정점
g = [[] for _ in range(N+1)] # 그래프
visited1 = [False]*(N+1) # dfs 방문 여부
visited2 = [False]*(N+1) # bfs 방문 여부

for i in range(M): # 간선수만큼 for문 돌려
    start, end = map(int,input().split()) # 양방향 연결된 노드까지 넣어 그래프 만들기
    g[start].append(end) # start에 연결되어 있는 노드
    g[end].append(start) # end에 연결되어 있는 노드
# print(g) # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
# print(g) # [[], [2, 3], [5, 1], [4, 1], [5, 3], [4, 2]]

def dfs(graph, v, visited): # dfs(그래프, 탐색 정점, 방문) # 3
    stack = [] # 후입선출 스택 (가장 깊은 정점 먼저 뽑기)
    visited[v] = True # 탐색 정점 방문 처리
    print(v, end=' ') # 방문된 점 출력 # 3
    for i in sorted(graph[v]): # 방문할 정점 여러개면 오름차순 정렬 # [1, 4]
        if not visited[i]: # i 방문하지 않았으면 # 1
            stack.append(i) # 스택에 추가
            dfs(graph, stack.pop(), visited) # 바로 뽑고 dfs함수로 다시 탐색 고
            # dfs(graph, i, visited) # dfs함수로 다시 탐색 고

dfs(g,V,visited1) # 깊은 부분 우선 탐색 # 3 1 2 5 4 

print() # 줄바꿈

from collections import deque # 선입선출
def bfs(graph, v, visited): # bfs(그래프, 탐색 정점, 방문) 
    queue = deque([v]) # 양쪽 삽입 삭제 연산 덱 자료구조 사용 
    visited[v] = True # 방문 처리
    while queue: # 큐에 값이 있는 동안 계속 돌려
        v = queue.popleft() # 탐색 정점에 큐의 먼저 들어가고 뽑힌 값 할당
        print(v, end=' ') # 방문된 점 출력 
        for i in sorted(graph[v]): # 방문할 정점 여러개면 오름차순 정렬
            if not visited[i]: # i 방문하지 않았으면 
                queue.append(i) # 큐에 추가하고
                visited[i] = True # 방문 처리
           
bfs(g,V,visited2) # 가까운 노드부터 우선 탐색 # 3 1 4 2 5
