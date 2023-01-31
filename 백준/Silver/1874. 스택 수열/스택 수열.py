import sys
n = int(input())
stack = []
sign = []
cnt = 1    
temp = True

for i in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num: 
        stack.append(cnt) # [1, 2, 3, 4]
        sign.append('+') # ['+','+','+','+']
        cnt += 1         # 4
    if stack[-1] == num: # 4 == 4
        stack.pop()      # [1, 2, 3]
        sign.append('-') # ['+','+','+','+','-']
    else:
        temp = False
        # [1,3,4,5] # 여기서 결과가 나지만 남은 입력값까지 다 받음
        #  cnt = 3
        # ['+','-','+','+','-','+','+','+']

if temp == False:
    print('NO')
else:
    for i in sign:
        print(i)

# 1234 ++++-
# 123 -
# 123456 ++-
# 12345678 ++-
# 1234567 -
# 12345 -
# 12 -
# 1 -
# [4, 3, 6, 8, 7, 5, 2, 1]