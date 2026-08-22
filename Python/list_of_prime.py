#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] → return [2, 3, 5, 7]
#A prime number is a number greater than 1 that is only divisible by 1 and itself.



def prime(lis1):
    a = []
    
    for j in lis1:
        if j<2:
            continue
        is_prime = True
        for i in range(2,j):
            if j%i==0:
                is_prime = False
                break
        if is_prime==True:
            a.append(j)
        
        
    return a

lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = prime(lis1)
print(result)   
