n = int(input())

if n == 1:
    print(1)
    exit()
if n == 2:
    print(3)
    exit()

dp = [0 for _ in range(n + 1)]

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + (2 * dp[i - 2])

print(dp[n] % 10007)

# 1: 1 
# 2: 3 
# 3: 5 
# 4: 11 
# 5: 21 
# 6: 43 
# 7: 85  
# 8: 171 
# 12 : 2731 
