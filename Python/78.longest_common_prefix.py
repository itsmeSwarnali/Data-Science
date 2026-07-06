#Given a list of strings, return the longest common prefix shared by all of them. If there's no common prefix, return an empty string. 
# Example: ["flower", "flow", "flight"] → "fl". ["dog", "car", "race"] → ""

def longest_common_prefix(string):
    a = []
    for i in range(len(string[0])):    # position 0, 1, 2...
        for s in string:  
            print("S", s)             # s = each string in the list
            if i >= len(s):            # s is too short
                return "".join(a)
            if s[i] != string[0][i]:  # character mismatch
                return "".join(a)
        a.append(string[0][i])  
    return a
        

string = ["flower", "flow", "flight"]

result = longest_common_prefix(string)
print(result)