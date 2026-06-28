# Given a number n, return the sum of all numbers from 1 to n using recursion 
# (not a loop).
# n=5 → 15 (because 1+2+3+4+5 = 15)
#n=1 → 1
#n=0 → 0

def sum_to_n_recursive(n):
    sum_to_n = 0
    if n == 0:
        return 0
    if n>0:
        sum_to_n = n + sum_to_n_recursive(n-1)
        return sum_to_n


n = 6

result = sum_to_n_recursive(n)
print(result)