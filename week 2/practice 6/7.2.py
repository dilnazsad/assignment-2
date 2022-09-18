a = input("enter your array:\n")
arr = a.split()
size = len(arr)

minimum = arr[0]
for i in range(1, size):
    if arr[i] < minimum:
        minimum = arr[i]

print("minimum element: ", minimum)

maximum = arr[0]
for i in range(1, size):
    if arr[i] > maximum:
        maximum = arr[i]

print("maximum element: ", maximum)
print(arr)
maximum, minimum = minimum, maximum
print(arr)