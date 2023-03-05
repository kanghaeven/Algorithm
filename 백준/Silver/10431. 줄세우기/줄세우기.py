P = int(input())
for p in range(1, P+1):
    T = list(map(int, input().split()))
    # print(T)
    cnt = 0
    for i in range(2, len(T)):
        for j in range(1, i):
            if T[j] > T[i]:
                # print('befor = ', T)
                a = T.pop(i)
                # print('i = ', i)
                # print('j = ', j)
                T = T[:j] + [a] + T[j:]
                # print('after = ', T)
                cnt += i-j
    print(f'{p} {cnt}')
