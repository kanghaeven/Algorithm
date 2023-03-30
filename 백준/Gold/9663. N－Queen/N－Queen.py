def dfs(x):
    global cnt
    if x == N:
        cnt += 1
        return
    
    for y in range(N):
        if board1[y] == board2[x-y] == board3[x+y] == 0:
            board1[y] = board2[x-y] = board3[x+y] = 1
            dfs(x+1)
            board1[y] = board2[x-y] = board3[x+y] = 0


N = int(input())
board1, board2, board3 = [[0 for _ in range(2 * N)] for _ in range(3)]
cnt = 0
dfs(0)

print(cnt)