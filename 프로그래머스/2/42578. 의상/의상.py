def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    
    answer = 1
    for j in dic.values():
        answer *= j + 1 # 해당 종류의 의상을 입지 않는 경우를 추가
            
    return answer - 1 # 모든 의상을 입지 않는 경우 제외