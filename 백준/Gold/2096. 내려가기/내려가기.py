import sys

input = sys.stdin.readline

n = int(input())

maxDp = [0] * 3
minDp = [0] * 3

maxTmp = [0] * 3
minTmp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            maxTmp[j] = a + max(maxDp[j], maxDp[j + 1])                       
            minTmp[j] = a + min(minDp[j], minDp[j + 1])
        elif j == 1:
            maxTmp[j] = b + max(maxDp[j - 1], maxDp[j], maxDp[j + 1])
            minTmp[j] = b + min(minDp[j - 1], minDp[j], minDp[j + 1])
        else:
            maxTmp[j] = c + max(maxDp[j], maxDp[j - 1])                       
            minTmp[j] = c + min(minDp[j], minDp[j - 1])
    
    for j in range(3):
        maxDp[j] = maxTmp[j]
        minDp[j] = minTmp[j]

print(max(maxDp), min(minDp))