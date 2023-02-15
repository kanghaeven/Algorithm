
N, K = map(int,input().split())
a = [int(input()) for _ in range(N)]
a = list(reversed(a))
# print(a) # [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

cnt = 0
for i in a:
    cnt += K // i 
    K = K % i
print(cnt)
# 4200 % 50000 == 0
# 4200 % 10000 == 0
# 4200 % 5000 == 0
# 4200 % 1000 == 200 (1000 * 4)
# 200 % 500 == 0
# 200 % 100 == 0 (100 * 2)

