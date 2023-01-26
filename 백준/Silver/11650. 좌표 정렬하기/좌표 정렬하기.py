import sys
one = []
n = int(input())
for i in range(n):
    one.append(list(map(int,sys.stdin.readline().split())))

one = sorted(one, key = lambda x: (x[0], x[1]))

for i in one:
    print(f'{i[0]} {i[1]}')