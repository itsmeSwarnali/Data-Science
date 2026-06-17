# Given a list of numbers, return the second smallest number.


def second_smallest(lis):
    min1 = max(lis)
    min2 = max(lis)
    for i in lis:
        if i<min1:
            min2 = min1
            min1 = i
        elif i<min2:
            min2 = i

    return min2


lis = [1, 5, 2, 3]

result = second_smallest(lis)
print(result)