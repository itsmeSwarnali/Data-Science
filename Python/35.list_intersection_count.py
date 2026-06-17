# Given two lists, return how many elements they have in common (count, not the list itself).
#[1, 2, 3, 4] and [3, 4, 5, 6] → 2 because 3 and 4 are common.


def list_intersect_count(lis1, lis2):
    a = []
    for i in lis1:
        if i in lis2:
            a.append(i)
    return (len(a))


lis1 = [1, 2, 3, 4, 6]
lis2 = [3, 4, 5, 6]

result = list_intersect_count(lis1, lis2)
print(result)
