import heapq
N = int(input())
cards = [int(input()) for _ in range(N)]

def cardssort(cards):
    h = []
    for card in cards:
        heapq.heappush(h, card)
    # print(h)    
    
    result = []
    for hh in range(len(h)-1):
        hap = heapq.heappop(h) + heapq.heappop(h)
        result.append(hap)
        heapq.heappush(h, hap)
        # print('r:', result)
        # print('h:', h)
        # print()
    return result
    
ans = cardssort(cards)

print(sum(ans))