#Given a list of numbers, return the missing number from 1 to n. 
# Example: [1,2,4,5] → 3


def missing_num(lis):
    n= max(lis)
    a = []
    for i in range(1, n+1):
        if i not in lis:
            a.append(i)
    return a

lis = [1,2,4,6]

result = missing_num(lis)
print(result)
