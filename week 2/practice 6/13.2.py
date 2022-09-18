a = input("enter your array:\n")
arr = list(map(int, a.split()))

for i in range(len(arr)):
    if arr[i] < 15:
        arr[i] *= 2

print('changed array:', arr)
