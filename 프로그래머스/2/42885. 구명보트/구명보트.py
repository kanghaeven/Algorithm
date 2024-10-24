from collections import deque

def solution(people, limit):
    island = deque(sorted(people)) # deque로 변환하여 O(1) 시간 복잡도로 pop(0)을 처리
    boat = 0
    cnt = 0
    
    while len(island) > 0:
        boat += island.pop() # 가장 무거운 사람을 먼저 태움
        
        if (len(island) > 0 and boat + island[0] <= limit):
            boat += island.popleft() # 가장 가벼운 사람도 함께 태움
            
        cnt += 1 # 보트 카운트
        boat = 0 # 보트 초기화
        
    return cnt