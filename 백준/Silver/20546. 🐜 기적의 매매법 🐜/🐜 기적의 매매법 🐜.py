import sys
input = sys.stdin.readline

cash = int(input())
stock = list(map(int, input().split()))

def solution(cash, stock):
    smcash, jhcash = cash, cash
    sm, jh = 0, 0 
    check = 0
    for i in range(len(stock)):
        if smcash >= stock[i]:
            share = smcash // stock[i]
            smcash -= share * stock[i]
            sm += share

        if i > 2:
            if stock[i] > stock[i-1] > stock[i-2] > stock[i-3]:
                jhcash += jh * stock[i]
                jh = 0
            elif stock[i] < stock[i-1] < stock[i-2] < stock[i-3]:
                share = jhcash // stock[i]
                jhcash -= share * stock[i]
                jh += share

    sm_total = smcash + sm * stock[-1]
    jh_total = jhcash + jh * stock[-1]

    if sm_total > jh_total:
        print("BNP")
    elif sm_total < jh_total:
        print("TIMING")
    else:
        print("SAMESAME")

solution(cash, stock)