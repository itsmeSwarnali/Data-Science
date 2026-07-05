# Given a nested dictionary (one level deep only), flatten it so all keys from nested dicts are brought to the top level. Use dot notation for nested keys. 
# Example: {"a": 1, "b": {"c": 2, "d": 3}} → {"a": 1, "b.c": 2, "b.d": 3}

def flatten_dic(dic1):
    dic2 = {}
    for keys, values in dic1.items():
        
        if type(values) != dict:
            dic2[keys] = values
        #print(dic2)
        if type(values) == dict:
            for key, value in values.items():
                dic2[keys+ "." +key] = value
    
    return dic2


    
  


dic1 = {"a": 1, "b": {"c": 2, "d": 3}}

result = flatten_dic(dic1)
print(result)