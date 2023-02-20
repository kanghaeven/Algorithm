from itertools import combinations_with_replacement
N = int(input())
a = [1, 5, 10, 50]
arr = list(combinations_with_replacement(a, N)) # 모든 가능한 조합을 구하는 모듈
# arr # [(1, 1), (1, 5), (1, 10), (1, 50), (5, 5), (5, 10), (5, 50), (10, 10), (10, 50), (50, 50)]

summ = []
for i in arr: 
    summ.append(sum(i)) #sum((1, 1))
# summ # [2, 6, 11, 51, 10, 15, 55, 20, 60, 100]

print(len(set(summ))) # 중복된 값 없애고 길이 출력