from itertools import permutations

def isPrimeN(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    n = [*numbers]
    arr = set()
    
    for i in range(1, len(n) + 1):
        c = [int(''.join([*j])) for j in [*set(list(permutations(n, i)))]]
        for j in c:
            arr.add(j)
            
    for a in arr:
        if a > 1 and isPrimeN(a) == True:
            answer += 1
        
    return answer