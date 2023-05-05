dxy = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
N, M, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
# print(info) # r, c, m, s, d
for k in range(K):
    arr = [[[] for _ in range(N)] for _ in range(N)]
    # 모든 파이어볼 자신의 방향 d로 속력 s칸 만큼 이동
    for a in range(M):
        info[a][0] = ((info[a][0]-1) + dxy[info[a][4]][0] * info[a][3]) % N
        info[a][1] = ((info[a][1]-1) + dxy[info[a][4]][1] * info[a][3]) % N
        arr[info[a][0]][info[a][1]].append(info[a])
        
    # 2개 이상 파이어볼 하나로 합치기
    newinfo = []
    for x in range(N):
        for y in range(N):
            if len(arr[x][y]) >= 2:
                mm, ss, odd, even = 0,0,0,0
                for ball in arr[x][y]:
                    mm += ball[2]
                    ss += ball[3]
                    if ball[4] % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                newm = mm //5
                news = ss // len(arr[x][y])
                if newm == 0:
                    continue
                if odd == len(arr[x][y]) or even == len(arr[x][y]):
                    newd = [0,2,4,6]
                else:
                    newd = [1,3,5,7]
                for d in newd:
                    newinfo.append([x, y, newm, news, d])
            elif len(arr[x][y]) == 1:
                newinfo.append(arr[x][y][0])
    info = newinfo
    M = len(info)

cnt = 0
for b in range(M):
    cnt += info[b][2]

print(cnt)