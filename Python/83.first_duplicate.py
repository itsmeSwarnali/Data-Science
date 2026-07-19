# Given a list, return the first element that appears 
# more than once (first by position of its second occurrence). 
# Example: [2, 3, 4, 2, 5, 3] → 2 (because 2 repeats first, at index 3). [1, 2, 3] → None


def first_dup(lis):
    seen = [] # seen = set()
    for i in lis:
        if i in seen:
            return i
        seen.append(i) #seen.add(i)
    return None


lis = [5, 5, 1, 2]

result = first_dup(lis)
print(result)


