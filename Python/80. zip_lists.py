# Given two lists, return a list of tuples pairing elements at the same index. Stop at the shorter list. 
# Example: [1, 2, 3], ["a", "b", "c"] → [(1, "a"), (2, "b"), (3, "c")]. [1, 2, 3], ["a", "b"] → [(1, "a"), (2, "b")]

def zip_lists(lis1, lis2):
    length = min(len(lis1), len(lis2))
    a = []
    for i in range(length):
        b = (lis1[i], lis2[i])
        a.append(b)
    return a

lis1 = [1, 2, 3]
lis2 = ["a", "b", "c"]

result = zip_lists(lis1, lis2)
print(result)