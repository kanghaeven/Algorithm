
x, y = map(int, input().split()) # 10 8 
n = int(input())
X = []
Y = []

for i in range(n):
    xy, position = map(int, input().split())
    if xy == 0: # 가로
        Y.append(position)
    else: # 세로
        X.append(position)
X.insert(0, 0)
Y.insert(0, 0)
X.append(x)
Y.append(y)
X.sort()
Y.sort()
maxX = []
for i in range(1, len(X)):
    gap = X[i] - X[i-1]
    maxX.append(gap)
maxY = []
for i in range(1, len(Y)):
    gap = Y[i] - Y[i-1]
    maxY.append(gap)

print(max(maxX) * max(maxY))