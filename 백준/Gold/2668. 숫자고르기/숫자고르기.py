import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]
visited = [0 for _ in range(N + 1)]
result = []

def dfs(start, path, visited):
    global result
    if visited[start]: # 이미 방문한 경우 종료
        if start in path: # 사이클 형성 확인
            result.extend(path[path.index(start):])
            # path.index(start) => start가 처음 등장한 위치 찾기
            # path[path.index(start):] => 그 위치부터 끝까지 자르기 (사이클 부분만 남김)
            # result.extend() => 결과 리스트에 리스트를 풀어서 여러 개의 요소를 추가
        return

    visited[start] = 1
    path.append(start)
    dfs(arr[start], path, visited)
    path.pop()

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, [], visited)

result.sort()
print(len(result))
for r in result:
    print(r)