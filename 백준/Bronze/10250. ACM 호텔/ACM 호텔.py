t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    room1 = n % h # 층
    room2 = n // h + 1 # 호
    if room1 == 0: # 0층은 없다
        room1 = h # 층
        room2 = n // h # 호
    print(f'{room1*100+room2}')