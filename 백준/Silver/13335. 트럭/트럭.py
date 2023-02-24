from collections import deque
N, W, L = map(int, input().split()) # 트럭 수, 다리 길이, 다리 최대하중
truck = deque(map(int, input().split())) # 건너지 않은 트럭
bridge = deque([0] * W) # 다리 건너는 트럭
cnt = 0 # 최단 시간

while sum(bridge) + sum(truck) != 0: # 
    bridge.popleft() # 다리에 있는 트럭 먼저 보내기
    if sum(bridge) + truck[0] <= L: # 최대하중보다 적게 트럭들이 다리 건널 수 있음
        go = truck.popleft() # 다리 건널 트럭
        truck.append(0) # 0을 넣어 트럭이 빠질 때 sum(truck)이 계산되지 않는 경우 고려
        bridge.append(go) # 다리 건널 트럭 다리 건너기
    else: # 최대하중보다 커진다면
        bridge.append(0) # 트럭이 다리를 건너지 못해 0 추가

    cnt += 1
print(cnt)

#     print(bridge, truck)
# 1
# deque([0, 7]) deque([4, 5, 6, 0])
# 2
# deque([7, 0]) deque([4, 5, 6, 0])
# 3
# deque([0, 4]) deque([5, 6, 0, 0])
# 4
# deque([4, 5]) deque([6, 0, 0, 0])
# 5
# deque([5, 0]) deque([6, 0, 0, 0])
# 6
# deque([0, 6]) deque([0, 0, 0, 0])
# 7
# deque([6, 0]) deque([0, 0, 0, 0])
# 8
