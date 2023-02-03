import sys
input = sys.stdin.readline
n = int(input()) # 계단 수

# 계단의 개수는 300이하의 자연수
stair = [0] * 301 # 점수의 합 
s = [0] * 301 # 점수

for i in range(n):
    s[i] = int(input()) # 점수 리스트에 입력된 점수 값 저장

stair[0] = s[0] # 1 # 점수 리스트의 첫번째 값

stair[1] = s[0] + s[1] # 1 -> 2 # 첫번째 점수와 두번째 점수의 합

# 최댓값(두번째 점수와 세번째 점수의 합(연속), 첫번째 점수와 세번째 점수의 합(건너뜀))
stair[2] = max(s[1] + s[2], s[0] + s[2]) # 2 -> 3, 1-> 3

# 연속 stair[i] = stair[i-3] + s[i-1] + s[i] (3번 연속되면 안됨)
# 건너뜀 stair[i] = stair[i-2] + s[i]

# stair[3] = max(stair[0] + s[2] + s[3], stair[1]+ s[3]) # 1 -> 3 -> 4, 2 -> 4
# stair[4] = max(stair[1] + s[3] + s[4], stair[2]+ s[4]) # 2 -> 4 -> 5, 3 -> 5


for i in range(3,n):
    stair[i] = max(stair[i-3] + s[i-1] + s[i], stair[i-2] + s[i])

print(stair[n-1]) # 인덱스 값이니까 n-1