
def check_palin(arr):

    length = len(arr)//2

    for i in range(0, length):
        
        if arr[i] != arr[len(arr)-1-i]:
            return False
        
    return True


n = input("Enter space seperated integer nums: ")
arr = list(map(int, n.split()))

print(arr)

result = check_palin(arr)
if result == True:
    print("the num is palindrom")
else:
    print("Not")



