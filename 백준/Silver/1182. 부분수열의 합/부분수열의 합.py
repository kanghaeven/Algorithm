
def subset(idx):
    global cnt
    if idx == N:
        # print('check: ', check)
        arr = []
        for i in range(N):
            if check[i] == 1:
                arr.append(A[i])
        if arr:
            if sum(arr) == S:
                # print(arr)
                cnt += 1
        return

    check[idx] = 0
    subset(idx+1)
    check[idx] = 1
    subset(idx+1)


N, S = map(int, input().split())
A = list(map(int, input().split()))
check = [0] * N
cnt = 0    
subset(0)

print(cnt)