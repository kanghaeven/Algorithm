dealer = input().split()
n_card = list(map(int,input().split()))

n_num = int(dealer[0])
m_num = int(dealer[1])

plus_list = []

for a in range(n_num):
    for b in range(a+1, n_num):
        for c in range(b+1, n_num):
            plus = n_card[a] + n_card[b] + n_card[c]
            if plus <= m_num:
                plus_list.append(plus)

plus_list = sorted(plus_list)

print(plus_list[-1])