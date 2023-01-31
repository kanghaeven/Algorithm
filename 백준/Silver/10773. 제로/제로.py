import sys
k = int(input())
stack = []
for i in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop(-1)
    else:
        stack.append(n)

total = 0
for j in stack:
    total += j
    
print(total)
