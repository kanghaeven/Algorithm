n = int(input())

card = [0] + list(map(int, input().strip().split(' ')))

dp = [0 for _ in range(n + 1)]

# i개의 카드를 구매하는 최적의 방법 찾기
for i in range(1, n + 1):
     # j번 카드팩을 샀을 때의 최대 비용을 비교하여 dp[i]를 갱신
    for j in range(1, i + 1):
        # dp[i]는 i개의 카드를 채우는 방법 중 최대 비용을 저장
        dp[i] = max(dp[i], dp[i - j] + card[j]) 

print(dp[-1])