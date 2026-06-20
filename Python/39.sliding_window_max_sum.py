# Given a list of numbers and a window size k, 
# return the maximum sum of any k consecutive elements.
# lis = [2, 1, 5, 1, 3, 2], k = 3
# ans: 9 (because 5+1+3=9 is the largest sum of any 3 consecutive elements)


def sliding_window_max_sum(lis, k):
    a = []
    for i in range(0,len(lis)-(k-1)):
        a.append(sum(lis[i:k+i]))

    return max(a)


lis = [2, 1, 5, 1, 3, 2]
k = 3

result = sliding_window_max_sum(lis, k)
print(result)
