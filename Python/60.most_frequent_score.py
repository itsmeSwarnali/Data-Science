# Given a list of exam scores, return the score that occurs most often. 
# If there's a tie, return any one of them.
# [85, 90, 85, 70, 85, 90] → 85

def most_freq(lis):
    dic = {}
    max = 0
    key = 0
    for i in lis:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    for keys, values in dic.items():
        if values>max:
            max=values
            key = keys
    return key

lis = [70, 90, 85, 85, 90]
result = most_freq(lis)
print(result)