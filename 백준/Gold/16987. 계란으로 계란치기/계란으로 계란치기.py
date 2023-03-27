import sys
input = sys.stdin.readline

def crack(idx):
    global ans
    if idx == N: # 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 종료
        cnt = 0
        for e in egg:
            if e[0] <= 0: # 깨진 계란의 수 카운트
                cnt += 1
        ans = max(ans, cnt) # 깰 수 있는 계란 최대 개수
        return
    
    if egg[idx][0] <= 0: # 들고 있는게 깨져있으면 다음 계란으로
        crack(idx+1)
        return

    flag = True # 꺠지지 않은 계란 있는지 확인
    for i in range(N):
        if i == idx: # 손에 든 계란 제외
            continue
        if egg[i][0] > 0: # 꺠지지 않은 계란 하나라도 있으면 False
            flag = False
            break
    
    if flag: # True면 다 꺠져있으므로 종료
        ans = max(ans, N-1) # 들고 있는 계란 빼고 다 N-1
        return

    # 계란 치기
    for i in range(N):
        if i == idx: # 손에 든 계란 제외
            continue
        if egg[i][0] <= 0: # 이미 꺠진 계란 제외
            continue

        # 계란으로 계란 치기
        egg[idx][0] -= egg[i][1]
        egg[i][0] -= egg[idx][1]
        crack(idx+1) # 한 칸 오른쪽 계란을 손에 들고 다시 진행
        egg[idx][0] += egg[i][1]
        egg[i][0] += egg[idx][1]


N = int(input()) # 계란 수
egg = [list(map(int, input().split())) for _ in range(N)] # 내구도 무게
ans = 0

crack(0) # 가장 왼쪽의 계란을 든다

print(ans)