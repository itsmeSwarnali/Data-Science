# Given a list of numbers, 
# return the maximum sum of any contiguous subarray 
# (a run of consecutive elements). 
# Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (the subarray [4, -1, 2, 1] gives the largest sum)
# [1, 2, 3, 4] → 10
# [-1, -2, -3] → -1 
# [3, -4, 5, -2, 6, -1, 8, -10, 2] → 16, [5, -2, 6, -1, 8]

def max_subarray(lis):
    max = float("-inf")
    a = []
    for i in range(len(lis)):
        for j in range(i,len(lis)):
            if sum(lis[i:j+1]) > max:
                max = sum(lis[i:j+1])
                a = lis[i:j+1]
    
                
    return max

lis = [3, -4, 5, -2, 6, -1, 8, -10, 2]

result = max_subarray(lis)
print(result)