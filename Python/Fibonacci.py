#Given a number n, return the first n Fibonacci numbers as a list.
# n = 7 → [0, 1, 1, 2, 3, 5, 8]

def fibo(n):
    a=0
    b=1
    arr = []
    arr.append(a)
    arr.append(b)

    for i in range(0, n-2):
        c =  a + b
        arr.append(c)
        a = b
        b = c
    return arr
    

n=7
result= fibo(n)
print(result)


