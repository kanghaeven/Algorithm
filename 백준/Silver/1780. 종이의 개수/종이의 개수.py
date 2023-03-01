m_cnt = 0
z_cnt = 0
p_cnt = 0

def check(x, y, N):
    first = paper[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != first:
                return False
    return True

def scissors(x, y, N):
    global m_cnt, z_cnt, p_cnt
    if check(x, y, N) == True:
        if paper[x][y] == -1:
            m_cnt += 1
        if paper[x][y] == 0:
            z_cnt += 1
        if paper[x][y] == 1:
            p_cnt += 1
        return

    new_N = N // 3
    scissors(x, y, new_N)
    scissors(x, y + new_N, new_N)
    scissors(x, y + new_N * 2, new_N)
    scissors(x + new_N, y, new_N)
    scissors(x + new_N, y + new_N, new_N)
    scissors(x + new_N, y + new_N * 2, new_N)
    scissors(x + new_N * 2, y, new_N)
    scissors(x + new_N * 2, y + new_N, new_N)
    scissors(x + new_N * 2, y + new_N * 2, new_N)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

scissors(0, 0, N)
print(m_cnt)
print(z_cnt)
print(p_cnt)