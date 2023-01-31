import sys
n = int(input())
deque = []

for i in range(n):
    user = sys.stdin.readline().split()

    if user[0] == 'push_front':
        deque.insert(0, int(user[1]))

    elif user[0] == 'push_back':
        deque.append(int(user[1]))

    elif user[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))

    elif user[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())

    elif user[0] == 'size':
        print(len(deque))

    elif user[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif user[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif user[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
