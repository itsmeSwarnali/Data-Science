#Given a 2D list (matrix) of numbers, return the number that appears most frequently across the entire matrix. 
# Example: [[1, 2, 1], [3, 1, 4], [2, 1, 5]] → 1 (appears 4 times)


def most_freq_in_mat(mat):
    dic = {}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] in dic:
                dic[mat[i][j]] += 1
            else:
                dic[mat[i][j]] = 1
    max = 0
    key = 0
    for keys, values in dic.items():
        if values>max:
            max = values
            key = keys
    return key


mat = [
        [5, 2, 5], 
        [3, 5, 4], 
        [2, 1, 5],
        [5,3,2]
    ]

result = most_freq_in_mat(mat)
print(result)
