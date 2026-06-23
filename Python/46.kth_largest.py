# Given a list of numbers and an integer k, 
# return the kth largest element (k=1 means the largest, k=2 means second largest, etc.).

def kth_largest(lis,k):
    sorted_lis = sorted(lis, reverse=True)
    return sorted_lis[k-1]

lis = [3, 1, 4, 1, 5, 9, 2]
k=3

result = kth_largest(lis,k)
print(result)
