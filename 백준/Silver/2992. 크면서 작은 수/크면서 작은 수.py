from itertools import permutations
X = input()

xx = list(permutations(X, len(X)))
a = []
ans = 0
for i in xx:
    if int(X) < int(''.join(i)):
        a.append(int(''.join(i)))
        ans = min(a)

print(ans)