#Problem 5: Given a list and an integer k, rotate the list to the right by k steps.

# [4, 5, 1, 2, 3]
def rotate_list(lis,k):
    
    rotate = lis[-k:]+lis[:-k]
    return rotate


lis = [1, 2, 3, 4, 5]
k = 2

result = rotate_list(lis,k)
print(result)
