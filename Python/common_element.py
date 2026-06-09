#Given two lists, return a list of elements that appear in both lists.
# No duplicates in the result.

# [1, 2, 3, 4] and [3, 4, 5, 6] → return [3, 4]
#Because 3 and 4 appear in both lists.
#[1, 2, 2, 3] and [2, 2, 4] → return [2]


def common_element(lis1, lis2):
    a = []
    for item in lis1:
        if item in lis2:
            if item not in a:
                a.append(item)
    
    return a

lis1 = [1, 2, 2, 4]
lis2 = [3, 2, 2, 6]

result = common_element(lis1, lis2)
print(result)

