N = int(input())
dp = [0] * (100001)

dp[1] = 3   # 3
dp[2] = 7   # 3 * 2 + 1   # dp[1] * 2 + 1
dp[3] = 17  # 7 * 2 + 3   # dp[2] * 2 + dp[1]
dp[4] = 41  # 17 * 2 + 7  # dp[3] * 2 + dp[2]

for i in range(5, N+1):
    dp[i] = (dp[i-1] * 2 + dp[i-2])%9901

print(dp[N])