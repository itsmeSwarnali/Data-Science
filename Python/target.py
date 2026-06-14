# Given a list of numbers, return all pairs that sum to a given target. 
# Example: [1,2,3,4], target=5 → [(1,4),(2,3)]


def target_tuple(lis, target):
    arr = []
    for i in  range(len(lis)):
        for j in range(i+1, len(lis)):
            if lis[i]+lis[j] == target:
                arr.append((lis[i], lis[j]))
    return arr



lis = [1,2,3,4]
target = 5

result = target_tuple(lis, target)
print(result)