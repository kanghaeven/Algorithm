H, W = map(int, input().split())
heights = list(map(int, input().split()))

s = 0 # 처음
mx = 0 # 최댓값
mxidx = 0 # 최댓값 인덱스
b = 0 # 빗물

# 최댓값을 구하고 -> 최댓값을 기준으로 전,후 나눠서 빗물 담기

for i in range(s, W): # 처음부터 끝까지 순회하며 최댓값, 인덱스 저장
    if heights[i] > mx: 
        mx = heights[i]
        mxidx = i

for j in range(s+1, mxidx): # 처음 + 1 부터 최댓값 전까지 순회하며 담긴 빗물 더하기
    if heights[s] > heights[j]: # 처음 값보다 탐색 값이 작으면
        b += heights[s] - heights[j] # 담긴 빗물 더하기
    else: # 처음 값보다 탐색 값이 크면
        s = j # 처음 값을 탐색값으로 업데이트

# 3 0 4 0 6 0 1
# 3 - 4 = -1 담기지 않는 부분 고려

while mxidx != W - 1: # 최댓값 인덱스 == 끝 -> 담길 공간 있을 동안 반복
    s = mxidx # 처음을 최댓값 인덱스로 없데이트
    mx = 0 # 담은 부분 이후부터 최댓값 다시 구하기

    if s+2 < W: # 담길 공간이 있을 때만 탐색
        for a in range(s+1, W): # 처음 + 1 부터 끝까지 순회하며 담긴 빗물 더하기
            if heights[a] > mx:
                mx = heights[a]
                mxidx = a
    else: # 담길 공간이 남아있지 않으면 종료
        break

    for c in range(s+1, mxidx):
        if heights[mxidx] > heights[c]:
            b += heights[mxidx] - heights[c]
        else:
            mxidx = c
print(b)
