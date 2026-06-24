# Given a nested list (multiple levels deep) and a target value, 
# count how many times the target appears anywhere in the structure. 
# Example: [1, 1, [2, 1, [1, 3]], 1, 1], target=1 → 4


def count_nested(lis, target):
    count = 0
    for i in range(len(lis)):
        if lis[i] == target:
            count += 1
        elif type(lis[i]) == list:
            x = count_nested(lis[i], target)
            count = x+count

    return count

lis = [1, 1, [2, 1, [1, 3]], 1, 1]
target = 2

result = count_nested(lis, target)
print(result)