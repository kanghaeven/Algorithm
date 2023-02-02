n = int(input())

def sugar(num):
    five = num // 5 # 5kg
    three = num // 3 # 3kg
    for i in range(three+1): # 3kg 수 늘리기
        for j in range(five+1): # 5kg 수 늘리기
            if 3 * i + 5 * j == num: # 입력값과 같다면
                return i + j # 총 개수 반환
    return -1 # 아니면 -1 반환

print(sugar(n))