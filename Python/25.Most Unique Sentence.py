# Given a list of sentences, 
# return the sentence with the most unique words


def unique_words(sentences):
    max = 0
    key = ""
    for sen in sentences:
        max_values = len(set(sen.split()))
        if max_values> max:
            max = max_values
            key = sen

    return key


sentences = [
    "the cat sat on the mat",
    "the quick brown fox",
    "hello world hello"
]

result = unique_words(sentences)
print(result)

    
    
    