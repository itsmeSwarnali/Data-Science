# Given a list and a chunk size k, split the list into sublists of size k. The last chunk may be smaller if the list doesn't divide evenly. 
# Example: [1,2,3,4,5,6,7], k=3 → [[1,2,3],[4,5,6],[7]]

def chunk_list(lis,k):
    a = []
    for i in range(0, len(lis),k):
        a.append(lis[i:k+i])
       
    return a
 
lis = [1,2,3,4,5,6,7]
k = 3

result = chunk_list(lis,k)
print(result)