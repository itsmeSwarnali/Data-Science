#Given a list, reverse it using recursion 
# (not slicing, not a loop with swapping — actual recursion). 
# Example: [1, 2, 3, 4] → [4, 3, 2, 1]


def reverse_recursive(lis):

    if len(lis)<=1: return lis
    reverse = []
    reverse.extend(reverse_recursive(lis[1:]))
    reverse.append(lis[0])
    
    return reverse

lis = [1, 2, 3, 4]
print(lis)
result = reverse_recursive(lis)
print(result)


"""
First it keeps breaking:

[1, 2, 3, 4]
→ [2, 3, 4]
→ [3, 4]
→ [4]   base case

Now [4] returns.

Then append starts while coming back:

For lis = [3, 4]:
reverse.extend([4])     → reverse = [4]
reverse.append(3)       → reverse = [4, 3]

For lis = [2, 3, 4]:
reverse.extend([4, 3])  → reverse = [4, 3]
reverse.append(2)       → reverse = [4, 3, 2]

For lis = [1, 2, 3, 4]:
reverse.extend([4, 3, 2]) → reverse = [4, 3, 2]
reverse.append(1)         → reverse = [4, 3, 2, 1]
"""