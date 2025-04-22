from itertools import product

def solution(word):
    aeiou = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(6):
        for j in list(product(aeiou, repeat=i)):
            arr.append(j)
    arr.sort()
    return arr.index(tuple(word))