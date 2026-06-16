# Problem 29 — Given a list of numbers, return a new list where each element is the running total. 
# Example: [1, 2, 3, 4] → [1, 3, 6, 10]

def running_total(lis1):
    lis2=[]
    lis2.append(lis1[0])
    for i in range(1, len(lis1)):
        lis2.append(lis1[i] + lis2[i-1])

    return lis2


lis1 = [1, 2, 3, 4] 
result = running_total(lis1)
print(result)