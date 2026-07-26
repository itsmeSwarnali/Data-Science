# Given a list of numbers and a target difference k, return the count of unique pairs where the absolute difference between the two numbers equals k. 
# Example: [1, 5, 3, 4, 2], k=2 → 3 (pairs: (1,3), (3,5), (2,4))

def count_pair_with_diff(lis,k):
    b = []
    a = []
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if abs(lis[i] - lis[j]) == k:
                a = (lis[j], lis[i])
                b.append(a)

    return len(b)


lis  = [1, 5, 3, 4, 2]
k=2
result = count_pair_with_diff(lis,k)
print(result)
