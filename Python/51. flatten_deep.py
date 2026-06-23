# Given a list that may contain lists nested at multiple levels (not just one level deep), 
# return a single fully flattened list
# [1, [2, [3,[4]]], 5] → [1, 2, 3, 4, 5]

def flatten_deep(lis):
    a=[]
    for i in range(len(lis)):
        print("Extend")
        if type(lis[i])!=list:
            a.append(lis[i])

        elif type(lis[i])==list:
            a.extend(flatten_deep(lis[i]))
            
        
    
    return a


lis = [1, [2, [3,[4]]], 5]
a = []


result = flatten_deep(lis)
print(result)