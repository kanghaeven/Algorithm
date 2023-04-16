N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i): # arr의 처음부터 i-1번째 인덱스까지
        if arr[i] > arr[j]: # 숫자의 크기를 비교하여 현재 값이 더 크면
            dp[i] = max(dp[i], dp[j] + 1) # dp배열의 값을 더 큰 값으로 갱신

print(max(dp))