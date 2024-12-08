import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(M)]

def solution(a, b, c):
    if a == 1:
        s[b - 1] = c
    if a == 2:
        for j in range(b-1, c):
            if s[j] == 0:
                s[j] = 1
            else:
                s[j] = 0
    if a == 3:
        for j in range(b-1, c):
            s[j] = 0
    if a == 4:
        for j in range(b-1, c):
            s[j] = 1

for i in range(len(arr)):
    solution(arr[i][0], arr[i][1], arr[i][2])

print(*s)