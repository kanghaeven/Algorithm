nine = [int(input()) for s in range(9)]
# print(nine)
nine.sort()
from itertools import combinations
seven = list(combinations(nine, 7))
# pprint(list(combinations(nine, 7)))

for s in seven:
    if sum(s) == 100:
        ans = s
        
for a in ans:
    print(a)