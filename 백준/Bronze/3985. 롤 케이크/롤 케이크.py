L = int(input()) # 롤케잌 길이
N = int(input()) # 방청객 
people = [list(map(int, input().split())) for n in range(N)]
cake = [0 for _ in range(L)]
# print(cake)
# print(people)
peice = []

for i in range(len(people)):
    for j in range(people[i][0]-1, people[i][1]):
        # print(people[i], people[i][0], people[i][1]+1, j, i)
        if cake[j] == False:
            cake[j] = i+1
        # print(j, cake[j])
        # print(cake)
    peice.append([i+1, people[i][1]-people[i][0]])

mx = 0
mxidx = 0
for i in range(len(peice)):
    if peice[i][1] > mx:
        mx = peice[i][1]
        mxidx = peice[i][0]
print(mxidx)
# print(cake)

mxcnt = []
for i in range(N):
    cnt = 0
    for j in range(len(cake)):
        if cake[j] == i+1:
            cnt += 1
    mxcnt.append([i+1, cnt])
# print(mxcnt)

actidx = 0
actmx = 0
for i in range(len(mxcnt)):
    if mxcnt[i][1] > actmx:
        actmx = mxcnt[i][1]
        actidx = mxcnt[i][0]
print(actidx)