
# 세로, 가로, 주사위 좌표, 명령 개수
N, M, x, y, K = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split())) # 명령 동 1 서 2 북 3 남 4


dice = [0,0,0,0,0,0,0] # 0 번 인덱스는 안씀
# dice = [안씀, 윗면, 북쪽, 동쪽, 서쪽, 남쪽, 아래]
#          _    1    2    3    4    5    6

def role_dice(before, direction): # 방향대로 주사위 굴리기
    # dice = [윗면, 북쪽, 동쪽, 서쪽, 남쪽, 아래]
    _, a, b, c, d, e, f = before
    if direction == 1 : # 동쪽
        after = [_, d, b, a, f, e, c]
    elif direction == 2 : # 서쪽
        after = [_, c, b, f, a, e, d]
    elif direction == 3 : # 북쪽
        after = [_, e, a, c, d, f, b]
    elif direction == 4 : # 남쪽
        after = [_, b, f, c, d, a, e]
    return after

# 명령대로 사방탐색 ,  0 번 인덱스는 안씀
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for k in range(K):
    direction = cmd[k] # 명령대로 방향 지정

    # 지도의 바깥으로 이동시킬 수 없다
    if 0 <= (x + dx[direction]) < N and 0 <= (y + dy[direction]) < M:
        x += dx[direction]
        y += dy[direction]
    
        dice = role_dice(dice, direction) # 주사위를 굴렸을 때

        if num[x][y] == 0: # 이동한 칸에 쓰여 있는 수가 0이면
            num[x][y] = dice[-1] #  주사위의 바닥면에 쓰여 있는 수가 칸에 복사
        else: # 0이 아닌 경우
            dice[-1] = num[x][y] # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
            num[x][y] = 0 # 칸에 쓰여 있는 수는 0

        print(dice[1]) # 상단에 쓰여 있는 값 출력
    
