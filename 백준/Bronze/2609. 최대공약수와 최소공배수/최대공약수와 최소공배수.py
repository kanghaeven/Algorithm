a, b = map(int,input().split(' '))
tmpa = a
tmpb = b

while a % b != 0:
    a, b = b, a % b

minn = tmpa * (tmpb // b)

print(b)
print(minn)
