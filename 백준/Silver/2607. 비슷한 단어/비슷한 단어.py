
N = int(input()) # 단어의 개수
first = list(input()) # 첫 번째 딘어
first.sort() # 알파벳 순 정렬
cnt = 0 # 비슷한 단어 개수

for a in range(N-1): 
    word = list(input()) # 비교할 단어
    word.sort()
    
    # 단어의 길이 맞추기
    if len(word) >= len(first): # 비교할 단어 길이 >= 첫 단어 길이면
        length = len(word) # 길이 = 비교할 단어 길이
    else: # 비교할 단어 길이 < 첫 단어 길이
        length = len(first) # 길이 = 첫 단어 길이
        
    # 단어 길이 만큼 돌려서 같으면 
    for i in range(len(first)): # 첫 단어 알파벳 하나씩 잡고 돌리기
        for j in range(len(word)): 
            if first[i] == word[j]:
               length -= 1 # 길이 -1
               word[j] = '' # 비교한 단어의 인덱스는 비우기
               break # 확인했으니까 멈추고 다음 첫 단어 알파벳으로

    if length <= 1: # 길이가 하나보다 작아야 비슷한 단어
        cnt += 1
print(cnt)

        
        
        