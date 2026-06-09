# Given a list of numbers, return True if any two numbers add up to a given target. 
# Otherwise return False.


#[1, 2, 3, 4] with target 7 → True because 3 + 4 = 7
#[1, 2, 3, 4] with target 10 → False because no two numbers add up to 10.

def two_list_add_target(lis, target):

    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if lis[i] + lis[j] == target:
                return True
    return False

lis = [1,5,2,4]
target = 9
result = two_list_add_target(lis, target)
print(result)
