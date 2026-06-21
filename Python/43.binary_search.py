# Given a sorted list of numbers and a target, 
# return the index of the target using binary search. 
# Return -1 if not found.
# [1, 3, 5, 7, 9, 11], target = 7 → return 3 (index of 7)
# [1, 3, 5, 7, 9, 11], target = 4 → return -1 (4 isn't in the list)

def binary_search(lis,target):
    low = 0
    high = len(lis)-1

    while low<=high:
        mid = (low+high)//2
        if lis[mid]==target:
            return mid
        elif lis[mid]<target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


lis = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(lis,target)
print(result)