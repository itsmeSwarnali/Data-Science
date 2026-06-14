# Given a sentence, reverse only the words not the characters. 
# Example: "hello world" → "world hello"

def reverse_sent(string):
    str1=string.split()
    arr = []
    for i in range(len(str1)-1,-1, -1):
        arr.append(str1[i])
    return arr


string = "hello world"

result = reverse_sent(string)
print(result)

    