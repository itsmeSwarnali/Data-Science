# Given a string representing a sentence, 
# return the length of the longest word.
# "the quick brown fox" -> 5
# "hi there world" → 5 (length of "there" or "world")

def longest_word_length(string):
    string = string.split()
    max = 0
    for i in string:
        if len(i)>max:
            max = len(i)
    return max
            

string = "the quick brown fox"

result = longest_word_length(string)
print(result)