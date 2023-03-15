import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(N)]

# 5가지 테트로미노 대칭 회전 모든 경우의 수의 합 구한 뒤 최댓값
mino = []


#### 대칭 x 
# ab = []
for a in range(N):
    for b in range(M-3):
        mino.append(sum(num[a][b:b+4]))
        # ab.append(num[a][b:b+4])
# print(ab)

# 대칭 x
#
#
#
for e in range(N-3):
    for c in range(M):
        cd = []
        for d in range(e, e + (N - (N-4))):
            cd.append(num[d][c])
        mino.append(sum(cd))
        # print(cd)


## 대칭 x 회전 x
##
for f in range(N - 1):
    for g in range(M - 1):
        hi = []
        for h in range(f, f+2):
            for i in range(g, g+2):
                hi.append(num[h][i])
        mino.append(sum(hi))
        # print(hi)


##  ##
#    #
#    #

#    #
#    #
##  ##
for j in range(N - 2):
    for k in range(M - 1):
        lm = []
        for l in range(j, j+3):
            for m in range(k, k+2):
                lm.append(num[l][m])
        # print(lm) # [1, 2, 5, 4, 2, 3]
        # 1 2  # idx 0 1
        # 5 4  # idx 2 3
        # 2 3  # idx 4 5
        mino.append(lm[0]+lm[1]+lm[2]+lm[4])
        mino.append(lm[0]+lm[1]+lm[3]+lm[5])
        mino.append(lm[0]+lm[2]+lm[4]+lm[5])
        mino.append(lm[1]+lm[3]+lm[4]+lm[5])
#    #
##  ##
 #  # 

#    #
##  ##
#    #
        mino.append(lm[0]+lm[2]+lm[3]+lm[5])
        mino.append(lm[1]+lm[2]+lm[3]+lm[4])
        mino.append(lm[0]+lm[2]+lm[3]+lm[4])
        mino.append(lm[1]+lm[2]+lm[3]+lm[5])


###  ###
#      #

#      #
###  ###
for n in range(N - 1):
    for o in range(M - 2):
        pq = []
        for p in range(n, n+2):
            for q in range(o, o+3):
                pq.append(num[p][q])
        # print(pq) # [1, 2, 3, 5, 4, 3]
        # 1 2 3  # idx 0 1 2 
        # 5 4 3  # idx 3 4 5
        mino.append(pq[0]+pq[1]+pq[2]+pq[3])
        mino.append(pq[0]+pq[1]+pq[2]+pq[5])
        mino.append(pq[0]+pq[3]+pq[4]+pq[5])
        mino.append(pq[2]+pq[3]+pq[4]+pq[5])
 ##     ###
##       #

##       #
 ##     ###
        mino.append(pq[1]+pq[2]+pq[3]+pq[4])
        mino.append(pq[0]+pq[1]+pq[4]+pq[5])
        mino.append(pq[0]+pq[1]+pq[2]+pq[4])
        mino.append(pq[1]+pq[3]+pq[4]+pq[5])

print(max(mino))