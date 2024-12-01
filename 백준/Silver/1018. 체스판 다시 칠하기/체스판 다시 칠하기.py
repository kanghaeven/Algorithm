N, M = map(int,input().split())
chess = [input() for _ in range(N)]
cnt = []

for n in range(N-7): # 8 * 8로 자르고 무슨 색으로 시작하는지 판별
    for m in range(M-7): 
        w = 0 # 흰색으로 시작
        b = 0 # 검은색으로 시작
        for i in range(n, n+8): # 세로열 중 i번째 시작 지점
            for j in range(m, m+8): # 가로열 중 i번째 시작 지점
                if (i+j) % 2 == 0: # 짝수인 경우 (0,0)
                    if chess[i][j] != 'W': # 검정이면
                        w += 1 # 흰색으로 칠하는 개수 카운트
                    else: # 흰색이면
                        b += 1 # 검정으로 칠하는 개수 카운트
                else: # 홀수인 경우 (0,1)
                    if chess[i][j] != 'W': # 검정이면
                        b += 1 # 검정으로 칠하는 개수 카운트
                    else: # 흰색이면
                        w += 1 # 흰색으로 칠하는 개수 카운트
        cnt.append(w) # 흰색으로 시작할 때 경우의 수
        cnt.append(b) # 검정으로 시작할 때 경우의 수 
print(min(cnt))

# 0,0 = 0 W  0,1 = 1 B  0,2 = 2 W  0,3 = 3 B 
# 1,0 = 1 B  1,1 = 2 W  1,2 = 3 B  1,3 = 4 W     
# 2,0 = 2 W  2,1 = 3 B  2,2 = 4 W  2,3 = 5 B
# 3,0 = 3 B  3,1 = 4 W  3,2 = 5 B  3,3 = 6 W 



# for i in range(M-8):
#     for j in range(i, M-i):
#         for k in range(N-8):
#             for q in range(k, N-k):
#                 if chess[k][q] == 'B':
#                     cntb += 1
#                 elif chess[k][q] == 'W':
#                     cntw += 1

# for m in range(M): 
#     for n in range(N-1):
#         if chess[m][n] == chess[m][n+1]:
#             while chess[m][n-1]:
#                 while chess[m][n] == chess[m][n+1] and chess[m][n] == chess[m][n-1]:
#                     cnt += 1
#                     break
#                 break
#             else:
#                 cnt += 1

# for n in range(N): 
#     for m in range(m-1):
#         if chess[m][n] == chess[m+1][n]:
#             while chess[m-1][n]:
#                 while chess[m][n] == chess[m+1][n] and chess[m][n] == chess[m-1][n]:
#                     cnt += 1
#                     break
#                 break
#             else:
#                 cnt += 1
