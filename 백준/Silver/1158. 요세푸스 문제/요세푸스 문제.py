from collections import deque
n, k = map(int, input().split())
people = deque() # 빈 큐 만들기
for i in range(1, n+1): # 1~n번 사람
    people.append(i)
jo = [] # 요세푸스 순열

while people: # 빈 큐는 False로 while loop 빠져나옴
    for j in range(k-1): # for문으로 k번만큼 순회
        people.append(people.popleft()) # (맨 처음 데이터 삭제 및 반환한 요소)를 맨 뒤에 추가
    jo.append(people.popleft()) # k번째 요소 추가로 요세푸스 순열 만들기

print(str(jo).replace('[','<').replace(']','>'))

# 1, 2, [3], 4, 5, 6, 7 --> 3 제거
# 1, 2, [3], 4, 5, [6], 7 --> 6 제거(6이 제거된 다음 7이 첫번째가 됨)
# 1, [2], [3], 4, 5, [6], 7 --> 2 제거
# 1, [2], [3], 4, 5, [6], [7] --> 7 제거
# 1, [2], [3], 4, [5], [6], [7] --> 5 제거
# [1], [2], [3], 4, [5], [6], [7] --> 1 제거
# [1], [2], [3], [4], [5], [6], [7] --> 4 제거