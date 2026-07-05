# Given a positive integer n, return a list of numbers counting down from n to 1, 
# built using recursion (no loops). 
# Example: 5 → [5, 4, 3, 2, 1]

def count_down(n):
    a = []
    b = []
    if n<1:return []
    a.append(n)
    a.extend(count_down(n-1))
   
    return a
n=5
result = count_down(n)
print(result)