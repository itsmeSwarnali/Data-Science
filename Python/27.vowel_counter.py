# Given a string, count how many vowels it contains.
# "hello world" → 3 because e, o, o are vowels.


def vowel_count(string):
    vowel = 'aeiouAEIOU'
   
    count = 0
    for i in range(len(string)):
        if string[i] in vowel:
            count+=1
    return count

string = "hello world"

result = vowel_count(string)
print(result)