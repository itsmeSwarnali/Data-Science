# Given a list of words, return only the words that are palindromes.
#["racecar", "hello", "level", "world", "madam"] → ["racecar", "level", "madam"]


def palindrome_words(list1):
    a = []
    for i in list1:
        if i == i[::-1]:
            a.append(i)
    return a


list1 = ["racecar", "hello", "level", "world", "madam"] 

result = palindrome_words(list1)
print(result)