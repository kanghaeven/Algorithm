N = int(input())
ppl = [list(map(int, input().split())) for n in range(N)]
# print(ppl) # [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]
result = []

for i in range(N): # 한 사람마다 다 돌면서 비교
    cnt = 0
    for j in range(N): # 덩치가 작을때 마다
        if ppl[i][0] < ppl[j][0] and ppl[i][1] < ppl[j][1]: # 몸무게 키 둘다 작으면
            cnt += 1 # 카운트
    result.append(cnt+1) # 덩치 등수는 +1
    print(result[i], end = ' ')