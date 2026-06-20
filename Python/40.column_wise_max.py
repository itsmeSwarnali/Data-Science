# Given a 2D list (matrix), 
# return a list with the maximum value from each column.
# matrix = [[1, 5, 2], [4, 1, 6], [3, 8, 0]]
# [4, 8, 6] (max of column 0: 1,4,3→4; column 1: 5,1,8→8; column 2: 2,6,0→6)

matrix = [[1, 5, 2], 
          [4, 1, 6], 
          [3, 8, 0]]

b= []
for i in range(len(matrix[0])):
    a=[]
    for j in range(len(matrix)):
        x = matrix[j][i]
        a.append(x)
    b.append(max(a))
print(b)
        