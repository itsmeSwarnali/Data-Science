# Given a list of numbers representing daily temperatures, 
# return True if the temperatures have been strictly rising 
# for at least k consecutive days at some point in the list. 
#(You'll need to decide: does this need the length of the run, or just whether one of at least length k exists anywhere?)
# [1, 2, 3, 1, 5, 6, 7, 8], k=3 → True

def has_increasing_run_k(lis, k):
    count = 1
    for i in range(len(lis)-1):
        if lis[i]<lis[i+1]:
            count = count+1

            if count==k:
                return True
            
        elif lis[i]>lis[i+1]:
            count = 1

    return False


lis = [1, 2, 3, 1, 5, 6, 7, 1]
k=4

result = has_increasing_run_k(lis, k)
print(result)
