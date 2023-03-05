n = int(input())
num = list(map(int, input().split()))
# 0 1 1 3 2 

# 4 2 5 3 1

lst = []

for i in range(n):
    lst.insert(num[i], i+1)
print(*list(reversed(lst)))