# Given a sentence, reverse each word's letters but keep the word order. 
# Example: "hello world" → "olleh dlrow"



def reverse_each_word(sen):
    sent = sen.split()
    a = []
    for i in sent:
        a.append(i[::-1])
    return " ".join(a)




sen = "hello world"

result = reverse_each_word(sen)
print(result)