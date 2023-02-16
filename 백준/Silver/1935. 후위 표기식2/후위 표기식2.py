N = int(input())
s = input()
num = [int(input()) for _ in range(N)]
# print(num) # [1, 2, 3, 4, 5]
stack = []
alpha_to_num = dict()
idx = 0
for i in s:

    if i.isalpha():
        if not alpha_to_num.get(i):
            alpha_to_num.setdefault(i, num[idx])
            idx += 1
        stack.append(alpha_to_num[i])
    else:
        if len(stack) >= 2:
            b = float(stack.pop())
            a = float(stack.pop())
            if i == '*':
                c = a * b
                stack.append(c)
            if i == '/':
                c = a / b
                stack.append(c)
            if i == '+':
                c = a + b
                stack.append(c)
            if i == '-':
                c = a - b
                stack.append(c)
        # print(c)
print(f'{stack[0]:.2f}')
