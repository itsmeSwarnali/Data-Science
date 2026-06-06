dic = {}

arr = [1,2,3,2,4,1,1,10]
a = []
for i in range(0, len(arr)):
    if arr[i] in dic:
        dic[arr[i]]+=1
    else:
        dic[arr[i]] = 1

for key, values in dic.items():
    if values>1:
        a.append(key)


print(a)
