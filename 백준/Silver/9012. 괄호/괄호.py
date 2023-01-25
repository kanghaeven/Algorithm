t = int(input())

for i in range(t):
    a = input()
    b = list(a)
    sum = 0

    for i in b:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            break   
    if sum == 0:
        print('YES')
    else:
        print('NO')