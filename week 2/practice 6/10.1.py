a = input("enter your array:\n")
arr = list(map(int, a.split()))

check = True
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            check = False
            print('duplicate element:', arr[i])

if check is True:
    print('no duplicate elements')
