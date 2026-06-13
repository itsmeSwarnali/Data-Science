#Given a list of strings, return the longest string. If there's a tie, 
# return the first one.

#["cat", "elephant", "dog", "hippopotamus"] → return "hippopotamus"

lis = ["cat", "elephant", "dog", "hippopotamus", "dfrekimfnslo"]
max = 0
key = 0
for i in lis:
    if len(i)>max:
        max = len(i)
        key = i


print(key)

