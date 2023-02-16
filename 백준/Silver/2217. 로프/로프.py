N = int(input()) 
w = [int(input()) for _ in range(N)]
# print(w) # [10, 15] 
a = []
# w.sort()
# w = list(reversed(w)) 
w.sort(reverse = True) # 내림차순 크기순대로 정렬
# 요소가 많을 때 정렬한 후 들 수 있는 무게에 대한 로프의 개수를 역순말고 쉽게 연산하기 위함
# [1, 3, 5, 17, 28, 78]
#  6  5  4  3   2   1
# print(w) # [15, 10] 
for i in range(1, N+1): 
    aa = w[i-1] * i
    a.append(aa) 
print(max(a))
