#Given a sentence as a string, return the most frequent word.
#"the cat sat on the mat the cat" → return "the" because it appears 3 times.

def freq_word(string):

    sen = string.split()

    dic = {}
    for word in sen:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    max = 0
    key = 0
    for keys, values in dic.items():
        if values>max:
            max = values
            key = keys
    return key


string = "the cat sat on the mat the cat"


result = freq_word(string)
print(result)
