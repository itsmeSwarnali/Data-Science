# Given a list of product prices, return True if any two prices add up 
# to exactly a given budget amount.
# [10, 25, 40, 15], budget = 50

def two_sum_exists(lis, budget):
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if lis[i]+lis[j]==budget:
                return True
    return False

lis = [10, 25, 40, 15]
budget = 100
result = two_sum_exists(lis, budget)
print(result)
