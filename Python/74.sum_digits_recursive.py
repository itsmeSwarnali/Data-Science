#Given a positive integer, return the sum of its digits using recursion. 
# Example: 1234 → 10 (because 1+2+3+4=10)
# "what's the simplest input where I already know the answer?" and 
# "how do I make the problem one step smaller?" Answer those two questions first, 

def sum_digit_recur(n):
    
    if n<10: return n
    sum = (n%10) + sum_digit_recur(n // 10)
    return sum

n = 1234

result = sum_digit_recur(n)
print(result)