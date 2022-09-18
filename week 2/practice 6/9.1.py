a = input("enter your array:\n")
arr = list(map(int, a.split()))

min = abs(arr[0])
minID = 0
for i in range(len(arr)):
    if abs(arr[i]) <= min:
        min = abs(arr[i])
        minID = i
print('absolute minimum element in array:', arr[minID])
arr.reverse()
print('reversed array: ', arr)
