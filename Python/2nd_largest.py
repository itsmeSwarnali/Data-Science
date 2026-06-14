

def second_largest(lis1):
    max1=0
    max2=0
    for i in range(len(lis1)):
        if lis1[i]>max1:
            max2 = max1
            max1 = lis1[i]
        elif lis1[i]>max2:
            max2 = lis1[i]
    return max2




lis1 = [1,2,5,4,3]

result = second_largest(lis1)
print(result)