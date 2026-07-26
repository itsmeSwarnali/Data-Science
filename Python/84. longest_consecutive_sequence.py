# Given an unsorted list of integers, return the length of the longest consecutive sequence. 
# Example: [100, 4, 200, 1, 3, 2] → 4 (the sequence 1, 2, 3, 4)

def longest_cons_seq(lis):

    sorted_list = sorted(lis)
    print(sorted_list)

    count = 1
    max = 0
    for i in range(len(sorted_list)-1):

        if sorted_list[i+1]-sorted_list[i]==0:
            continue
        
        elif sorted_list[i+1]-sorted_list[i]==1:
            count += 1
            if count>max:
                max = count
        elif sorted_list[i+1]-sorted_list[i] > 1:
            count = 1
            
    return max

lis = [1, 1,2, 3, 4, 9, 10, 20]

result = longest_cons_seq(lis)
print("result: ",result)


