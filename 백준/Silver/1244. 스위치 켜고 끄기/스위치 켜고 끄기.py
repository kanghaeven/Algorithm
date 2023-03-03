# 남학생 스위치 번호 % 받은 수 == 0  -> 스위치 바꿈
# 여학생 스위치 번호 == 받은 수 중심 -> 대칭 스위치 바꿈
# 대칭이 없으면 스위치 번호 == 받은 수 바꿈


swi_num = int(input())
switch = list(map(int, input().split()))
switch.insert(0,0)
stu_num = int(input())
stu_info = [list(map(int, input().split())) for _ in range(stu_num)]
# print(switch)
# print(stu_info)

for i in range(stu_num):
    if stu_info[i][0] == 1: # 남
        for s in range(1, swi_num+1): # 스위치 인덱스 순회
            if s % stu_info[i][1] == 0: # 남 스위치 번호 % 받은 수 == 0 
                if switch[s] == 1: # 스위치 바꿈
                    switch[s] = 0
                else:
                    switch[s] = 1
# print(switch) # [0, 0, 1, 1, 1, 0, 1, 0, 1]

    if stu_info[i][0] == 2: # 여
        s = stu_info[i][1] # 여 스위치 번호 == 받은 수
        if switch[s] == 1: # 스위치 바꿈
            switch[s] = 0
        else:
            switch[s] = 1

        for j in range(1, swi_num + 1):
            if 0 < s-j and s+j < swi_num + 1:
                if switch[s-j] == switch[s+j]: # 양 옆 대칭
                    if switch[s+j] == 1: # 스위치 바꿈
                        switch[s+j] = 0
                        switch[s-j] = 0
                    else:
                        switch[s+j] = 1
                        switch[s-j] = 1
                else:
                    break

for t in range(1, swi_num+1, 20):
    print(*switch[t: t+20])
