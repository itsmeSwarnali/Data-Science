# Given two dictionaries where each value is a list, merge them so that if a key exists in both, 
# the lists are combined (not summed). 
# Example: {"a": [1,2], "b": [3]} and {"a": [4], "c": [5]} → {"a": [1,2,4], "b": [3], "c": [5]}


def dic_value_list_merge(dic1, dic2):
    dic3 = {}
    a=[]
    for keys, values in dic1.items():
        if keys in dic2:
            dic3[keys] = values
        else:
            dic3[keys] = values

    for key, value in dic2.items():
        if key in dic3:
            dic3[key].extend(value)
        else:
            dic3[key] = value
    
    return dic3
            



dic1 = {"a": [1,2,6], "b": [3]} 
dic2 = {"a": [7], "c": [5]}

result = dic_value_list_merge(dic1, dic2)
print(result)