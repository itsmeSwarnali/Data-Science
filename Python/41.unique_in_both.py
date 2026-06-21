# Given two lists, return elements that appear in exactly 
# one of the two lists (not in both). 
# Example: [1,2,3], [2,3,4] → [1, 4]


def unique_in_both(lis1, lis2):
    a = []

    for i in lis1:
        if i not in lis2:
            a.append(i)

    for i in lis2:
        if i not in lis1:
            a.append(i)

    return a

lis1 = [1,2,3,5]
lis2 = [2,3,4,5]

result = unique_in_both(lis1, lis2)
print(result)