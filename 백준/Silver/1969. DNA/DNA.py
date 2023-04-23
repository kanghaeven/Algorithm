
import sys
input = sys.stdin.readline

dna_num, string_num = map(int, input().split())
whole_dna = []
for _ in range(dna_num):
    new = list(input())
    whole_dna.append(new)


# Hamming Distance의 합이 가장 작은 DNA란
# 각 위치의 뉴클오티드 문자가 가장 많이 나오는 걸 구하는 것과 같다.

cnt = 0
result = ''

for i in range(string_num):
        acgt = [0, 0, 0, 0]
        # dna_num개의 dna 중에서 가장 많이 나온 뉴클레오티드 구하기
        for j in range(dna_num):
            if whole_dna[j][i] == 'A':
                acgt[0] += 1
            if whole_dna[j][i] == 'C':
                acgt[1] += 1
            if whole_dna[j][i] == 'G':
                acgt[2] += 1
            if whole_dna[j][i] == 'T':
                acgt[3] += 1                
        
        idx = acgt.index(max(acgt))
        # print(acgt)
        
        # Hamming Distance의 합이 가장 작은 dna 구하기
        if idx == 0:
            result += 'A'
        elif idx == 1:
            result += 'C'
        elif idx == 2:
            result += 'G'
        elif idx == 3:
            result += 'T'

        # Hamming Distance 계산하기
        cnt += dna_num - max(acgt)
        # print(cnt)
        
print(result)
print(cnt)

'''
# string_num만큼의 길이인 리스트에 / 무작위로 'A', 'T', 'G', 'C'가 들어간 

nucleotide = ['A', 'T', 'G', 'C']
number = []
for a in range(string_num):
    for b in range(a, string_num):
        for c in range(b, string_num):
            for d in range(c, string_num):
                if a + b + c + d == string_num:
                    number.append([a, b, c, d])      

from itertools import permutations
# cnt_min = []
cnt_mn = 10000000
cnt_mn_arr = []
for n in number:
    # print(n)
    for aa, tt, gg, cc in permutations(n, 4):
        arr = []
        for aaa in range(aa):
            arr.append('A')
        for ttt in range(tt):
            arr.append('T')
        for ggg in range(gg):
            arr.append('G')
        for ccc in range(cc):
            arr.append('C')

        for p in permutations(arr, string_num):
            cnt = 0
            for s in range(string_num):
                for w in range(dna_num):
                    if p[s] != whole_dna[w][s]:
                        cnt += 1
            if cnt_mn > cnt:
                 cnt_mn = cnt
                 cnt_mn_arr = p
            # cnt_min.append(cnt)
# print(min(cnt_min))

print(*cnt_mn_arr)
print(cnt_mn)
'''