
N = int(input()) # 색종이 수
point = [list(map(int, input().split())) for _ in range(N)]
paper = [[0 for _ in range(100)] for _ in range(100)]

for n in range(len(point)):
    a = point[n]
    # print(a)
    for x in range(100):
        for y in range(100):
            if y == a[0] and x == a[1]:
                for xx in range(a[1], a[1]+10): # 0 ~ 10 == 3 ~ 13
                    for yy in range(a[0], a[0]+10):
                        paper[xx][yy] = 1

# pprint(paper)

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)