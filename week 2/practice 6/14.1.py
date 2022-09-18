a = input("enter your array:\n")
arr = list(map(int, a.split()))

max = arr[0]
mxindex = 0
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
        mxindex = i

min = arr[0]
mnindex = 0
for j in range(len(arr)):
    if arr[j] < min:
        min = arr[j]
        mnindex = j

print('the maximum value:', max)
print('the minimum value:', min)
arr[mnindex] = max
arr[mxindex] = min
print('swapped array:', arr)
