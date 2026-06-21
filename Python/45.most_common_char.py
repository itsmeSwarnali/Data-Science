# Given a string, 
# return the character that appears most frequently (ignore spaces).
# string = "hello world",  "l" (appears 3 times, more than any other character; spaces are ignored)

string = "hello worlddd"
dic = {}
gap = " "
for i in string:
    if i in dic and i not in gap :
        dic[i] += 1
    elif i not in gap:
        dic[i] = 1

max = 0
key = 0
for keys, values in dic.items():
    if values>max:
        max = values
        key = keys
print(key)
        

        
