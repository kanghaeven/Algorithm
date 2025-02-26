# 1 1
# 2 2
# 3 4
# 4 7 = 1 + 2 + 4
# 5 13 = 2 + 4 + 7
# 6 24 = 4 + 7 + 13
# 7 44 = 7 + 13 + 24

t = int(input())
dp = [0 for _ in range(12)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(t):
    n = int(input())
    if dp[n] == 0:
        for i in range(4, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    print(dp[n])
