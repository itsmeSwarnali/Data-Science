# Two strings are anagrams if they contain the exact same characters in any order.
#"listen" and "silent" → True because both have: e, i, l, n, s, t
#"hello" and "world" → False because different characters.

def anagram(string1, string2):

    dic1 = {}
    dic2 = {}

    for i in range(len(string1)):
        if string1[i] in dic1:
            dic1[string1[i]]+=1
        else:
            dic1[string1[i]]=1


    for j in range(len(string2)):
        if string2[j] in dic2:
            dic2[string2[j]]+=1
        else:
            dic2[string2[j]]=1



    if dic1==dic2:
        return True
    else:
        return False
    
    #or only "return dic1==dic2"



string1 = "listens"
string2 = "silent"

result = anagram(string1, string2)
print(result)
