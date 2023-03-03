N = int(input()) # 색종이의 수
position = [list(map(int, input().split())) for _ in range(N)]
paper = [[0 for _ in range(100)] for _ in range(100)]

for p in position:
    for x in range(100):
        for y in range(100):
            if y == p[0] and x == p[1]:
                for xx in range(p[1], p[1] + 10):
                    for yy in range(p[0], p[0] + 10):
                        paper[xx][yy] = 1

# for row in paper:
#     print(*row)

# 점을 센다 생각하고 모서리도 포함한 둘레를 구해야 함
dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            one_cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < 100 and 0 <= ny < 100:
                    if paper[nx][ny] == 1:
                        one_cnt += 1
            if one_cnt == 3:
                cnt += 1
            if one_cnt == 2:
                cnt += 2

print(cnt)