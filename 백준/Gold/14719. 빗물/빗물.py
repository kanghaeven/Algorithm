H, W = map(int, input().split())
heights = list(map(int, input().split()))

s = 0
mx = 0
mxidx = 0
b = 0

for i in range(s, W):
    if heights[i] > mx:
        mx = heights[i]
        mxidx = i

for j in range(s+1, mxidx):
    if heights[s] > heights[j]:
        b += heights[s] - heights[j]
    else:
        s = j


while mxidx != W - 1:
    s = mxidx
    mx = 0

    if s+2 != W:
        for a in range(s+1, W):
            if heights[a] > mx:
                mx = heights[a]
                mxidx = a
    else:
        break

    for c in range(s+1, mxidx):
        if heights[mxidx] > heights[c]:
            b += heights[mxidx] - heights[c]
        else:
            mxidx = c
print(b)
