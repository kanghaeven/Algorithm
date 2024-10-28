def solution(citations):
    ans = 0
    citations.sort(reverse=True)    # 역정렬로 큰 순서대로
    
    for i in range(len(citations)):
        if (citations[i] > ans):    # 현재 H-index보다 순회하는 값이 크면
            ans = i + 1             # 현재 H-index = 순회하는 인덱스 + 1
        else:                       # 현재 H-index보다 순회하는 값이 같거나 작으면
            break                   # 현재 H-index로 리턴하기 위해 멈춤
    return ans