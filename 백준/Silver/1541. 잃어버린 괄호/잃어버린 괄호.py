input = input().split('-')
# print(input)

for i in range(len(input)):
    for j in input[i]:
        if j == '+':
            plus = input[i].split('+')
            # print(plus)
            for p in range(len(plus)):
                plus[p] = int(plus[p])
            input[i] = sum(plus)
            break
    # print(input[i])
    # print(type(input[i]))
# print(input)
for u in range(len(input)):
    input[u] = int(input[u])
ans = input[0] - sum(input[1:])
print(ans)