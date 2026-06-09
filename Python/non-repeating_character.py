
Given a string, return the first non-repeating character. 
If all characters repeat, return None.


def non_repeat_char(str):
    a = {}

    for char in str:
        if char in a:
            a[char] += 1
        else:
            a[char] = 1

    for char in str:
        if a[char] == 1:
            return char
    return None
str = "swwiiss"

non_repeat = non_repeat_char(str)
print(non_repeat)
