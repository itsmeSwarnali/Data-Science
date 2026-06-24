# Given a number n, return its factorial using recursion (not a loop). 
# Example: 5 → 120 (because 5×4×3×2×1=120)


def factorial_recur(n):
    a = 1
    if n == 0:
        return 1
    
    elif n!=0:
        a = n * factorial_recur(n-1)
    
    return a

n = 5
#print(n)
result = factorial_recur(n)
print(result)