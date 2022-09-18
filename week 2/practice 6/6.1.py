a = input("enter your array:\n")
arr = list(map(int, a.split()))

arr.sort()
print('maximum element in array:', arr[len(arr) - 1])

arr.sort(reverse=True)
print('minimum element in array:', arr[len(arr) - 1])
