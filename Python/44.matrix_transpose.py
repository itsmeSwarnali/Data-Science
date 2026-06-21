# matrix_transpose.py — Given a 2D list (matrix), 
# return its transpose (rows become columns).

def matrix_trans(matrix):
    
    b = []
    for i in range(len(matrix[0])):
        a = []
        for j in range(len(matrix)):
            a.append(matrix[j][i])
        b.append(list(a))
    
    return b


matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]

result = matrix_trans(matrix)
print(result)