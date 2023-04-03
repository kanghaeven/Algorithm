
from itertools import combinations

N = int(input())
mp, mf, ms, mv = map(int, input().split())

nutrient = []
for _ in range(N):
    p, f, s, v, c = map(int, input().split())
    nutrient.append((p, f, s, v, c))

mn = 1000000
idx = []
for i in range(1, N+1):
    for com in combinations(range(N), i):
        arr = [0 for _ in range(5)]
        # print(com)
        # print(nutrient)
        for c in com:
            arr[0] += nutrient[c][0]
            arr[1] += nutrient[c][1]
            arr[2] += nutrient[c][2]
            arr[3] += nutrient[c][3]
            arr[4] += nutrient[c][4]

        if arr[0] >= mp and arr[1] >= mf and arr[2] >= ms and arr[3] >= mv:
            if mn > arr[4]:
                mn = arr[4]
                ans = mn
                idx = com
            elif mn == arr[4]:
                idx = sorted((idx, com))[0]

if mn == 1000000:
    ans = -1

print(ans)
if idx:
    for id in idx:
        print(id + 1, end=' ')

