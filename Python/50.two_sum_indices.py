# Given a list of numbers and a target, return the indices (not values) of the two numbers that add up to the target.
#
def two_sum_indices(lis, target):
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if lis[i]+lis[j]==target:
                return (i, j)

lis = [5,6,2,4,3]
target = 8
result = two_sum_indices(lis, target)
print(result)