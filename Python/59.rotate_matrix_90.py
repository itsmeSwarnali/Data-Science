# Given a square matrix, rotate it 90 degrees clockwise. 
# Example: [[1,2],[3,4]] → [[3,1],[4,2]]

def rotate_mat_90(mat):
    a = []
    b = []
    #x= []
    for i in range(len(mat)-1,-1,-1):
        x = []
        for j in range(len(mat[i])-1,-1,-1):
            x.append(mat[j][i]) # after reverse it jump to the cols not rows because of [j][i]
        a.append(list(x))
        #print(a)

    for i in range(len(a)-1,-1,-1):
        b.append(a[i])

    return b

mat = [[1,2],
       [3,4]]
result = rotate_mat_90(mat)
print(result)