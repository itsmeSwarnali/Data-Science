#Given a list of numbers and a divisor d, group the numbers by their remainder 
# when divided by d. 
# Example: [1, 2, 3, 4, 5, 6], d=3 → {1: [1, 4], 2: [2, 5], 0: [3, 6]}


def group_by_remainder(lis, d):
    dic = {}
    remainder = 0
    for i in range(len(lis)):
        remainder = lis[i]%d
        if remainder in dic:
            dic[remainder].append(lis[i])
        if remainder not in dic:
            dic[remainder] = []
            dic[remainder].append(lis[i])
    return dic

lis =  [1, 2, 3, 4, 5, 6]
d = 3
result = group_by_remainder(lis, d)
print(result)