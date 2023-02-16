N = int(input())
plan = [list(map(int,input().split())) for _ in range(N)]
plan = sorted(plan, key = lambda x:(x[1],x[0])) # 끝나는 시간 기준으로 오름차순 정렬
# print(plan) # [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

cnt = 0

for i in range(N):
    if i == 0:
        cnt += 1
        end = plan[i][1] # 4
        continue
        # 1, <4>
        # 4 <= <5>, 7
    if end <= plan[i][0]: # 4 5
        cnt += 1
        end = plan[i][1] # 11

print(cnt)