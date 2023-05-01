
N = int(input())
road = list(map(int, input().split())) 
station = list(map(int, input().split())) 


ans = 0
for i in range(N-1):
    # print('나는 i:', i)
    if station[i] < station[i+1] and station[i] > road[i+1]:
        ans += station[i] * (road[i]+1)
        # print('if:', station[i], road[i] + 1)
    # elif i == N and station[i+1] <= road[i]:
        # ans += station[i] * (road[i] + 1)
        # print('elif:', station[i], road[i] + 1)
    else:
        ans += station[i] * road[i]
        # print('else:', station[i] * road[i])
    # print(ans)
print(ans)