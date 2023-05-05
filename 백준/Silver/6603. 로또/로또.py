from itertools import combinations
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    k = arr[0]
    s = arr[1:]
    
    for lotto in combinations(s, 6):
        print(*lotto)
    print()