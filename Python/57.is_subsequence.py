# Given two strings, check if the first is a subsequence of the second 
# (characters appear in order, but not necessarily consecutively). 
# Example: "ace", "abcde" → True (a, c, e appear in that order). "aec", "abcde" → False

def is_subseq(string1, string2):
    if len(string1)==0:
        return True
    a = []
    i = 0
    for j in range(len(string2)):
        if string2[j] == string1[i]:# aec, abcde, for this case S2 will reach at the end but S1 will be in index 1, so i != len(S1)
            #a.append(i)
            i += 1
            #print(a)
            if i == len(string1): ## i cannot be == len(string1) if string2[j] != string1[i]
                return True # it only returns true when i reach to the end of S1, and to reach to the end all the char should be matched to S2 and that is how i increased i += 1

    return False

string1 = "ace" # aec
string2 = "acede" # acedc

result = is_subseq(string1, string2)
print(result)