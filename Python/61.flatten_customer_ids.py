#Given a list of customer IDs that may contain nested groups 
# (a customer ID might itself be a list of related sub-IDs, nested arbitrarily deep), 
# return one flat list of all individual IDs.
# [101, [102, 103],[105,106], 104] → [101, 102, 103, 104]

def flatten_ids(nested_lis):
    a = []
    for i in range(len(nested_lis)):
        if type(nested_lis[i]) != list:
            a.append(nested_lis[i])
        else:
            a.extend(flatten_ids(nested_lis[i]))
    return a

nested_lis = [101, [102, 103],[105,106], 104]

result = flatten_ids(nested_lis)
print(result)