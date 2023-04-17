from bisect import bisect_left
N = int(input())
arr = list(map(int, input().split()))

dp = [1]
x = [arr[0]]

for i in range(1, N):
    if arr[i] > x[-1]: # 현재 값이 x 배열의 마지막 값보다 클 경우
        x.append(arr[i])
        dp.append(dp[-1] + 1)
    else: # 현재 값이 x 배열의 마지막 값보다 작을 경우
        idx = bisect_left(x, arr[i]) # 현재 값이 x 배열의 몇 번째 인덱스에 들어갈 수 있는지 찾아서
        x[idx] = arr[i] # x 배열의 ids 위치에 현재 값을 넣어줌
print(len(x))