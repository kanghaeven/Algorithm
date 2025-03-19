n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

# 길이가 1인 경우, 각 숫자는 하나의 오르막수
for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1): # i 길이
    for j in range(10): # j 오르막수의 개수
        dp[i][j] = sum(dp[i - 1][0:j + 1]) # 0부터 j까지의 합

# print(dp)

print(sum(dp[n]) % 10007)