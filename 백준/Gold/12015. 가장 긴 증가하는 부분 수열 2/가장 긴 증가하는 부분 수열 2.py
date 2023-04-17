from bisect import bisect_left
N = int(input())
arr = list(map(int, input().split()))

x = [arr[0]] # 증가하는 부분 수열

for i in range(1, N):
    # 현재 값이 x 배열의 마지막 값보다 클 경우
    if arr[i] > x[-1]: 
        x.append(arr[i])

    # 현재 값이 x 배열의 마지막 값보다 작을 경우
    else:
        # 현재 값 arr[i]이 오름차순으로 x 배열의 몇 번째 인덱스에 들어갈 수 있는지 = idx
        idx = bisect_left(x, arr[i])
        x[idx] = arr[i] # x 배열의 idx 위치에 현재 값을 넣어줌

print(len(x))
# print(x) # [10, 20, 30, 50]