import sys
stack = []
n = int(input())

for i in range(n):
    user = sys.stdin.readline().split()

    if user[0] == 'push':
        stack.append(user[1])
    
    elif user[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif user[0] == 'size':
        print(len(stack))

    elif user[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif user[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])