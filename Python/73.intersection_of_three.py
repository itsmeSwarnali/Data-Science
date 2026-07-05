#  Given three lists, return a list of elements that appear in all three. No duplicates in the result. 
# Example: [1,2,3,4], [2,3,5], [2,3,6] → [2,3]

def intersec_of_three(lis1,lis2,lis3):
    #dic = {}
    a = []
    for i in lis1:
        if i in lis2:
            if i in lis3:
                if i not in a:
                    a.append(i)

    return a
lis1 = [1,2,3,3,4]
lis2 = [2,3,3,5]
lis3 = [2,3,6]

result = intersec_of_three(lis1,lis2,lis3)
print(result)