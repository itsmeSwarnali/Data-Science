#Given a sentence, return a dictionary with the count of each word.
# "the cat sat on the mat" → {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}



def word_freq(sen):
    sent = sen.split()
    dic = {}
    for i in sent:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
    return dic
    




sen = "the cat sat on the mat"

result = word_freq(sen)
print(result)
