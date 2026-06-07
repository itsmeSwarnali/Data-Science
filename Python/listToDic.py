
words = ["guava", "orange", "banana", "apple", "cherry"]
dic = {}
a = []
for word in words:
    if len(word) in dic:
        dic[len(word)].append(word)
    else:
        dic[len(word)] = [word]

print(dic)

""""
What you just learned:
A dictionary whose values are lists is one of the most common patterns in Data Science. We can see it constantly in grouping, 
aggregation, and data processing.
We now know it from the inside out — not from reading it, but from struggling to build it yourself. That's the difference.

"""
       
