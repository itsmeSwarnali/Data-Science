# Given a list of integers, return True if the list is sorted in ascending order.
# [1, 2, 3, 4, 5] → True
# [1, 3, 2, 4, 5] → False because 3 comes before 2.

def sorted_check(lis):
    for i in range(len(lis)-1):
        if lis[i] > lis[i+1]:
            return False
    return True

lis = [1, 2, 3, 2, 4, 5]

result = sorted_check(lis)
print(result)