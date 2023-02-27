
N = int(input()) # 지방 수
budget = list(map(int, input().split())) # 예산 요청
M = int(input()) # 총 예산

budget.sort() # 오름차순
left = 0 
right = max(budget)

while left <= right: # 이분 탐색
    mid = (left + right) // 2 # 상한액 
    money = 0 # 새로운 예산 총액

    for i in budget: 
        if i >= mid: # 요청 금액이 상한액 이상이라면
            money += mid # 상한액 더하기
        else: # 상한액 미만이라면
            money += i # 요청 금액 더하기
    
    if money <= M: # 예산 총액이 총 예산 이하라면
        left = mid + 1 # 상한액 높이기
    else: # 예산 총액이 총 예산을 초과한다면
        right = mid - 1 # 상한액 낮추기

print(right) # 예산 중 최대값


# sum(budget) > M
    # a = (M - sum(budget[:mid])) 
    # b = a // len(budget[mid+1:])