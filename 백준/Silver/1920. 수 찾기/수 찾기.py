import sys
n = int(input())
a = set(map(int, sys.stdin.readline().split()))
m = int(input())
aa = list(map(int, sys.stdin.readline().split()))

for i in aa:
    if i in a:
        print(1)
    else:
        print(0)