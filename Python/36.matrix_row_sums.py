# Given a 2D list (matrix) of numbers, return a list with the sum of each row.
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [6, 15, 24] (sum of each row)


def matrix_row_sum(matrix):
    a = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
        a.append(sum)
    return a


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = matrix_row_sum(matrix)
print(result)



