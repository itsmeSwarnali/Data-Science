# Given a list, return a dictionary where each key is a duplicated value and 
# the value is a list of all indices where it appears. 
# Example: [1, 2, 1, 3, 2] → {1: [0, 2], 2: [1, 4]}

def find_dup_ind(lis):
    dic = {}
    for i in range(len(lis)):
        if lis[i] not in dic:
            dic[lis[i]] = []
        
        dic[lis[i]].append(i)
        
    for key,value in list(dic.items()):
        if len(value)==1:
            dic.pop(key, None)
    return dic
lis = [1, 2, 1, 3, 2]

result = find_dup_ind(lis)
print(result)
