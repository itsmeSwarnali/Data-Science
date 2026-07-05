# Given two numbers base and exp, 
# return base raised to the power exp, using recursion (not ** or pow()). 
# Example: power_recursive(2, 5) → 32
#power_recursive(2, 5) → 32 (because 2×2×2×2×2 = 32)
#power_recursive(3, 0) → 1 (any number to the power of 0 is 1)
#power_recursive(5, 1) → 5

def power_recursive(base,exp):
    
    multi = 1

    if exp == 0:
        return 1
    
    multi = base * power_recursive(base,exp-1)

    return multi

base = 3
exp = 0

result = power_recursive(base,exp)
print(result)