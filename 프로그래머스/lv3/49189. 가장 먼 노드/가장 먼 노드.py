from collections import deque
def solution(n, edge):
    answer = 0

    adjL = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    
    for e in edge:
        adjL[e[0]].append(e[1])
        adjL[e[1]].append(e[0])

    q = deque([1])
    visited[1] = 1
    while q:
        node = q.popleft()
        for i in adjL[node]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[node] + 1
            
    print(visited) # [0, 1, 2, 2, 3, 3, 3]
    # print(adjL) # [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]
    return visited.count(max(visited))