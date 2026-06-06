
def check_dup(arr):
    a = []
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                a.append(arr[i])

    return set(a)

numbers = input("Enter some numbers: ")
arr = list(map(int, numbers.split()))

result = check_dup(arr)
print("result:", result)
