# Given a list of numbers, return the index of a "peak" element — one that is greater than its neighbors. 
# For the first and last elements, only one neighbor exists. Example: [1, 3, 2, 5, 4] → 3 (index of 5, since 5 > 2 and 5 > 4). Any valid peak index is acceptable if multiple exist.

def find_peak_element(lis):
    #max = 0
    index = 0
    for i in range(len(lis)):
        if len(lis) == 1:
            index = i
            #max = lis[i]
        if i==0 and len(lis) != 1:
            if lis[i]>lis[i+1]:
                #max = lis[i]
                index = i
        elif i==len(lis)-1:
            if lis[i-1]<lis[i]:
                #max = lis[i]
                index = i
        elif lis[i-1]<lis[i] and lis[i+1]<lis[i]:
            #max = lis[i]
            index = i
        
    return index

lis = [1, 3, 2, 5, 4]

result = find_peak_element(lis)
print(result)

