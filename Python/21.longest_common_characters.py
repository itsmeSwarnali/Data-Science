#Problem 21 — Given two strings, return the longest common characters between them.
#"hello" and "world" → ['l', 'o']


def longest_common_character(st1, st2):
    a = []
    for item in st1:
        if item in st2:
            if item not in a:
                a.append(item)
    return a

st1 = 'hello'
st2 = 'world'

result = longest_common_character(st1, st2)
print(result)
