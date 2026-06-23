# Given a list of numbers and a window size k, 
# return a list of the average of every k consecutive elements. 
# Example: [1, 2, 3, 4, 5], k=2 → [1.5, 2.5, 3.5, 4.5]

def moving_avg(lis, k):

    a = []
    for i in range(len(lis)-(k-1)):
        summ = 0
        summ = sum(lis[i:k+i])
        a.append(summ/k)

    return a

lis = [1, 2, 3, 4, 5]
k = 2

result = moving_avg(lis, k)
print(result)
