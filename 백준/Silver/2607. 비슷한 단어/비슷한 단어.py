N = int(input()) # 단어의 개수
first = list(input())
first.sort()
cnt = 0
for a in range(N-1):
    word = list(input())
    word.sort()
    
    if len(word) >= len(first):
        length = len(word)
    else:
        length = len(first)
        
    for i in range(len(first)):
        for j in range(len(word)):
            if first[i] == word[j]:
               length -= 1
               word[j] = ''
               break

    if length <= 1:
        cnt += 1
print(cnt)
