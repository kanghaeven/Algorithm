m_cnt, z_cnt, p_cnt = 0, 0, 0

def check(x, y, N): # 종이가 모두 같은 수로 되어 있는지 확인
    first = paper[x][y] # 첫 값이랑 비교

    for i in range(x, x + N): # x부터 x+N까지 순회
        for j in range(y, y + N):
            if paper[i][j] != first: # 같지 않으면
                return False # 거짓 반환
    return True # 다 같으면 참 반환

def scissors(x, y, N): # 같은 크기의 종이 9개로 자르고, 확인 과정 반복
    global m_cnt, z_cnt, p_cnt
    if check(x, y, N): # 모두 같은 수로 되어있으면 개수 카운트
        if paper[x][y] == -1:
            m_cnt += 1
        if paper[x][y] == 0:
            z_cnt += 1
        if paper[x][y] == 1:
            p_cnt += 1
        return # 함수 끝내줌
    # 아니면 같은 크기의 9개로 자르기
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