from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))
x = [arr[0]]

for i in range(1, n):
    if arr[i] > x[-1]:
        x.append(arr[i])
    else:
        idx = bisect_left(x, arr[i])
        x[idx] = arr[i]
        
print(len(x))