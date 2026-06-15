# Problem 22 — Given a number, return True if it is a palindrome. 
# Example: 121 → True, 123 → False



def is_palin(num):
    num = str(num)
    if num[::-1]==num[::]:
        return True
    else: return False
    

num = 12331

result = is_palin(num)
print(result)


""""

num = 12331
num = str(num)
a = []
for i in range(len(num)-1,-1,-1):
    a.append(num[i])

for i in range(len(num)):
    is_palin = True
    if num[i]!=a[i]:
        is_palin = False
        break
    else: is_palin = True

print(is_palin)

"""
