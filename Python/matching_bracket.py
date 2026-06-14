
def maching_brac(string):
    #strings = string.split()
    count = 0

    for str in string:
        if str == '(':
            count+=1
        elif str == ')':
            count-=1
            if count < 0:
                return False
    if count == 0:
        return True
    else: 
        return False

    

string = "(())(())"

result = maching_brac(string)
print(result)