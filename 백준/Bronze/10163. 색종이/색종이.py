
N = int(input())
# paper = [list(map(int, input().split())) for _ in range(N)]
area = [[0 for _ in range(1001)] for _ in range(1001)]
# print(area)

for n in range(1, N+1):
    paper = list(map(int, input().split()))

    for a in range(paper[0],paper[0]+paper[2]):
        for b in range(paper[1], paper[1]+paper[3]):
            area[a][b] = n
    # pprint(area)


for n in range(1, N+1):
    cnt = 0
    for x in range(1001):
        for y in range(1001):
            if area[x][y] == n:
                cnt += 1
    print(cnt)