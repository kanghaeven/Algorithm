
N, M, D = map(int, input().split()) # N 행  M 열  D 공격거리 제한
_pan = [list(map(int, input().split())) for _ in range(N)] + [[2] * M] # N행 성 2

su = [] # 성이 있는 궁수 3명이 배치될 수 있는 좌표 모두 구하기
for x in range(N+1):
    for y in range(M):
        if _pan[x][y] == 2:
            su.append([x, y])

mx = []
dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

from itertools import combinations
for i in combinations(su, 3): # 궁수 3명이 배치될 수 있는 경우 하나씩 순회
    cnt = 0
    flag = True # 겜 시작
    xx = N # 첫턴 궁수 기준 설정
    pan = [arr[:] for arr in _pan] # 깊은 복사 
    while flag: # 한 턴
    
        enemy = [] # 거리가 D이하인 적 중에서 가장 가까운 적, 여럿일 경우에는 가장 왼쪽에 있는 적 
        for b in range(M): # 왼쪽부터
            for a in range(xx-1, -1, -1): # 아래에서부터 위로 
                if pan[a][b] == 1:
                    enemy.append((a, b)) # set은 가변이안되는 형식만 이용가능->튜플

        attack = set() # 같은 적이 공격당할 경우 중복 빼기위해 set
        for goongsu in i: # 공격할 적 탐색
            yy = goongsu[1] 
            length = D+1 # 최솟값
            ee = None # 궁수가 잡을 적 좌표
            for e in enemy:
                aa, bb = e
                distance = abs(xx-aa) + abs(yy-bb)
                if distance <= D: # 조건
                    if distance < length: # 최솟값
                        length = distance # 가장 가까이 있는 적
                        ee = e # 가장 가까이 있는 적을 구할 때 마다 적의 좌표 업데이트

            attack.add(ee) # 공격당할 적 모두 담기

        for ac in attack: # 적 공격 : 0 처리
            if ac:
                pan[ac[0]][ac[1]] = 0
                cnt += 1 # 공격한 적 카운트
        xx -= 1 # 한 턴이 끝나면, 궁수가 위로 한 칸 이동

        flag = False # 게임 끝이라 가정
        for v in range(xx): 
            for z in range(M):
                if pan[v][z] == 1: # 공격할 적이 있으면
                    flag = True # 한 판 더 !
                    break 
            if flag == True: # 한 판 더 할거니까
                break # for문 그만돌리고 한 판 더 하러 ㄱ

    mx.append(cnt) # (궁수 배치 경우마다 공격한 적)


print(max(mx)) # (궁수 배치 경우마다 공격한 적)의 최대 수


