# Given a string, return a dictionary with the count of vowels and consonants.
#"hello world" → {"vowels": 3, "consonants": 7}

def count_vowels_consonant(sen):
    vowel = "aeiouAEIOU"
    consonant = " "
    count1 = 0
    count2 = 0
    for i in sen:
        if i in vowel:
            count1+=1
        if i not in vowel and i not in consonant:
            count2+=1

    dic = {
        "vowels": count1,
        "consonants": count2
    }
    return dic


sen = "hello world"

result = count_vowels_consonant(sen)
print(result)
