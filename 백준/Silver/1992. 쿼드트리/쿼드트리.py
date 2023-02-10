
def check(matrix):
    first = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != first:
                return False
    return True

def new(row_s, row_e, col_s, col_e, matrix):
    result = []
    for i in range(row_s, row_e):
        result.append(matrix[i][col_s:col_e])
    return result

def divide1(matrix):
    if check(matrix) == True:
        print(matrix[0][0],end="")
        return matrix[0][0]
    else: # check(matrix) == False: # 나눠서 0,1 출력
        len_new_matrix = len(matrix) // 2
                
        node1 = new(0, len_new_matrix, 0, len_new_matrix, matrix)
        node2 = new(0, len_new_matrix, len_new_matrix, len(matrix), matrix)
        node3 = new(len_new_matrix, len(matrix),0, len_new_matrix, matrix)    
        node4 = new(len_new_matrix, len(matrix),len_new_matrix, len(matrix), matrix)

        print('(', end='')
        divide1(node1)
        divide1(node2)
        divide1(node3)
        divide1(node4)
        print(')', end='')

N = int(input())
matrix = [list(map(int, list(input()))) for _ in range(N)]
divide1(matrix)
print()





# def check2(row, col, size):
#     first = matrix[row][col]
#     for i in range(row, row+size):
#         for j in range(col,col+size):
#             if matrix[i][j] != first:
#                 return False
#     return True

# def divide2(row, col, size):
#     if check2(row,col,size):
#         print(matrix[row][col],end='')
#         return
#     else:
#         new_size = size//2
#         print('(', end='')
#         divide2(row, col, new_size)
#         divide2(row, col+new_size, new_size)
#         divide2(row+new_size, col, new_size)
#         divide2(row+new_size, col+new_size,new_size)
#         print(')', end='')

# divide2(0,0,8)


