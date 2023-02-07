# 연결되어 있는 모든 컴퓨터 바이러스 걸림
# 1번과 연결되어 있는 자손 노드 수 출력

computers = int(input()) # 컴퓨터의 수
edges = int(input()) 
connect = [list() for i in range(computers + 1)]
visited = [False for i in range(computers + 1)]

for tc in range(edges):
    start, end = map(int, input().split())
    connect[start].append(end)
    connect[end].append(start)
# print(connect) [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

cnt = 0
def virus(num): # 1
    global cnt # 최상위 카운트에 접근
    virus_com = []
    # [2, 5]
    visited[num] = True # 1 
    for j in connect[num]: # [1] # [2]
      if visited[j] == False:
        cnt += 1
        virus_com.append(j)
        virus(virus_com.pop())
            
virus(1)
print(cnt)
