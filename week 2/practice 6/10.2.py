a = input("enter your array:\n")
arr = list(map(int, a.split()))

for i in range(len(arr)):
    if arr[i] < 10:
        arr[i] = 0
    elif arr[i] > 20:
        arr[i] = 1
print('changed array:', arr)
