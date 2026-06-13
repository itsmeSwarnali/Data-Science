# Given a dictionary, return a new dictionary with keys and values swapped.
# {"a": 1, "b": 2, "c": 3} → {1: "a", 2: "b", 3: "c"}


dic= {
    "a": 1, "b": 2, "c": 3
}

dic2 = {}
for keys, values in dic.items():
    dic2[values]= keys    
print(dic2)
