T = int(input())

memo = [0] * 11

def plus(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    
    if memo[x] != 0:
        return memo[x]
    
    memo[x] = plus(x-1) + plus(x-2) + plus(x-3)
    return memo[x]

for i in range(T):
    N = int(input())
    print(plus(N))