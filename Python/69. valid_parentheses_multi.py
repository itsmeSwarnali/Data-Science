# Given a string containing (, ), [, ], {, }, return True if all brackets are balanced and correctly matched (not just counted — "([)]" should be False even though counts match, because the types are mismatched).
# "([{}])" → True
# "([)]" → False
# "{[}]" → False

def valid_parentheses(string):
    a = []
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '{' or string[i] == '[':
            a.append(string[i])
            #print(a)
        else:
            if a == []: return False
            pop = a.pop()
            if string[i] == ')':
                if pop != '(':
                    return False

            elif string[i] == '}':
                if pop != '{':
                    return False

            elif string[i] == ']':
                if pop != '[':
                    return False
            
    if a == []:
        return True
    else: return False


string = ")"

result = valid_parentheses(string)
print(result)