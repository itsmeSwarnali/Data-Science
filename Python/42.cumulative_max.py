# Given a list of numbers, return a list where 
# each element is the maximum seen so far. 
# Example: [3, 1, 4, 1, 5, 9, 2] → [3, 3, 4, 4, 5, 9, 9]

def cululative_max(lis):
    a =[]
    num = lis[0]
    for i in lis:
        if i>num:
            num=i
        
        a.append(num)
            
            
    return a

lis = [3, 1, 4, 1, 5, 9, 2]
print(len(lis)-1)
result = cululative_max(lis)
print(result)