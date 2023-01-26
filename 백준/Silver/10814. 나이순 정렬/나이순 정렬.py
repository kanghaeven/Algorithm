import sys
n = int(input())
people = list()
for i in range(n):
    people.append(list(sys.stdin.readline().split()))

for i in people:
    i[0] = int(i[0])

people.sort(key=lambda x: x[0])

for i in people:
    print(f'{i[0]} {i[1]}')