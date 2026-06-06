def flatten(lis):
    a = []
    for i in range(len(lis)):
        if type(lis[i]) != list:
            a.append(lis[i])
        elif type(lis[i]) == list:
            for j in range(len(lis[i])):
                a.append(lis[i][j])

    return a
    

lis = [1,2, [4,5], 9]

result = flatten(lis)
print(result)
