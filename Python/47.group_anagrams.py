# Given a list of words, group them into anagram groups. 
# Example: ["eat", "tea", "tan", "ate", "nat", "bat"] → [["eat","tea","ate"], ["tan","nat"], ["bat"]]

def group_anagram(lis):
    dic = {}
    for i in lis:
        item = "".join(sorted(i)) # aet, abt, aet
        if item not in dic: #aet, #abt
            dic[item]=[]
        dic[item].append(i) ##eat, bat

    a = []
    for keys, values in dic.items():
        a.append(values)

    return a
lis = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = group_anagram(lis)
print(result)
