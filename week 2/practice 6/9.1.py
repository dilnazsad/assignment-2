a = input("enter your array:\n")
arr = a.split()
size = len(arr)

minimum = arr[0]
for i in range(1, size):
    if arr[i] < minimum:
        minimum = arr[i]

arr.reverse()
print("reversed array: ", arr)
print("minimum element: ", minimum)
