N = int(input())
S = [[0] + list(map(int, input().split())) for _ in range(N)]
S.insert(0, [0 for _ in range(N+1)])
# pprint(S)

start = []
link = []

num = [i for i in range(1, N + 1)]

from itertools import combinations # 중복 없는 순열
# print(list(combinations(num, N // 2)))
arr = list(combinations(num, N // 2))


for i in range(len(arr) // 2):
    start.append(arr[i])
    link.append(arr[-(i+1)])

mn = []
for a in range(len(start)):
    start_power = 0
    link_power = 0    
    compare = 0
    for b in start[a]:
        for c in start[a]:
            start_power += S[b][c]
    for d in link[a]:
        for e in link[a]:
            link_power += S[d][e] 
    compare = abs(start_power - link_power)
    mn.append(compare)
print(min(mn))
