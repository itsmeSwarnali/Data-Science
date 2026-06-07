
Given a non-empty list, return the element that appears most often. If there's a tie, 
return any one of them.


  
lis = [5,7,3,3,7,7,5,5,2]
a = {}
for i in range(len(lis)):
    if lis[i] in a:
        a[lis[i]] += 1
    else:
        a[lis[i]] = 1
print(a)

max_count = 0
key = 0
for keys, values in a.items():
    if values>max_count:
        max_count = values
        key = keys
        
print(key)


