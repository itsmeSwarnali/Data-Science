# Given two already-sorted lists, return a single sorted merged list without using .sort() or sorted(). 
# Example: [1, 3, 5], [2, 4, 6] → [1, 2, 3, 4, 5, 6]. 
# [1, 5, 9], [2, 3, 4] → [1, 2, 3, 4, 5, 9]

def merge_sorted_list(lis1, lis2):
    a = []
    i=0
    j=0

    while i<len(lis1) and j<len(lis2):
        
        if lis1[i]<lis2[j]:
            a.append(lis1[i])
            i = i+1
                
        elif lis1[i]>lis2[j]:
                a.append(lis2[j])
                j= j+1
            
    a.extend(lis1[i:])

    a.extend(lis2[j:])

    return a


lis1 = [1, 3, 5, 8, 9]
lis2 = [2, 4, 6, 7]

result = merge_sorted_list(lis1, lis2)
print(result)