# Given a nested list (multiple levels deep) of numbers, return the sum of all numbers using recursion. 
# Example: [1, [2, 3, [4, 5]], 6, 3] → 21

def sum_nested_recursive(lis):
    sum = 0
    for i in range(len(lis)):
        if type(lis[i]) != list:
            sum += lis[i]
        elif type(lis[i]) == list:
            x = sum_nested_recursive(lis[i])
            sum = x + sum


    return sum

lis = [1, [2, 3, [4, 5]], 6, 3]
result = sum_nested_recursive(lis)
print(result)