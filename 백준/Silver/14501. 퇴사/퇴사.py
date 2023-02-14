# DP
N = int(input())

t = []
p = []
dp = [0 for _ in range(N+1)]
# dp의 각 원소는 해당 날짜부터 퇴사일까지 받을 수 있는 최대 돈
# 뒤에서부터 N-1로 접근할 때 범위에서 벗어나지 않고 dp[i+1]을 참조하기 위해 N+1

for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)
# print(t) # [3, 5, 1, 1, 2, 4, 2]
# print(p) # [10, 20, 10, 20, 15, 40, 200]

for i in range(N-1, -1, -1): # 퇴사일을 넘지 않도록 뒤에서부터 역순으로
    if t[i] + i > N: # 상담 기간이 퇴사일 초과면 # 오늘날짜 + 상담 기간
        dp[i] = dp[i+1] # 상담을 못하니까 다음날 값 그대로 가져오기
    else: # 상담을 할 수 있으면
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i]) 
        # 오늘 상담 안하는 경우 dp[i+1] 다음날 값
        # 오늘 상담 하는 경우 (t[i] 상담 기간 + i 오늘 날짜) + 받을 돈
        # 중 최대값

print(dp[i])
# # Brute Force