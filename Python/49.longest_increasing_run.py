# Given a list of numbers, return the length of the longest run of strictly increasing consecutive numbers. 
# Example: [1, 2, 3, 1, 2, 5, 6, 7, 8] → 4 (the run 2,5,6,7,8... actually 5,6,7,8)

def longest_increasing_run(lis):
    count = 1
    max_count = 0

    for i in range(len(lis)-1):

        if lis[i+1]>lis[i]:
            count += 1
            #max_count += 1
            if count>max_count:
                max_count = count
                
        elif lis[i+1]<lis[i]: count = 1
            
    return max_count


lis = [5, 6, 7, 1, 2, 1]  # [1, 2, 1, 2, 5, 6, 7, 8, 1]

result = longest_increasing_run(lis)
print(result)



