# Given two dictionaries, merge them. 
# If a key exists in both, sum the values.
# dic1 = {"a": 1, "b": 2, "c": 3}
# dic2 = {"b": 4, "c": 1, "d": 5}
# ans: {"a": 1, "b": 6, "c": 4, "d": 5}



dic1 = {"a": 1, 
        "b": 2, 
        "c": 3}

dic2 = {"b": 4, 
        "c": 1, 
        "d": 5}
dic3 = {}

for keys, values in dic1.items():
    dic3[keys] = values
print(dic3)

for keys, values in dic2.items():
    if keys in dic3:
        dic3[keys] += values
    else: 
        dic3[keys] = values
print(dic3)