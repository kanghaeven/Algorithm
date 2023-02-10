def check(row, col, size):

    first = paper[row][col]

    for i in range(row, row + size):
        for j in range(col, col+size):
            if paper[i][j] != first:
                return False
    return True

blue = 0
whe = 0

def divide(row, col, size):
    global blue, whe
    if check(row, col, size) == True:
        if paper[row][col] == 0:
            whe += 1
        else:
            blue += 1
        return
    
    new_size = size // 2
    divide(row, col, new_size)
    divide(row, col + new_size, new_size)
    divide(row + new_size, col, new_size)
    divide(row + new_size, col + new_size, new_size)


N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
divide(0, 0, N)
print(whe)
print(blue)
# pprint(paper)