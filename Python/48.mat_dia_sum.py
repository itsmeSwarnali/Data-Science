#matrix diagonal sum.
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]] == 15

def mat_dia_sum(mat):
    sum=0
    for i in range(len(mat)):
        sum += mat[i][i]
    return sum
    
mat = [[1, 2, 3], 
       [4, 6, 6], 
       [7, 8, 7]]

result = mat_dia_sum(mat)
print(result)