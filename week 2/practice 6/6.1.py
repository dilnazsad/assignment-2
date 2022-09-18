a = input("enter your array:\n")
arr = a.split()
size = len(arr)

maximum = arr[0]
for i in range(1, size):
    if arr[i] > maximum:
        maximum = arr[i]

print("maximum element: ", maximum)

for i in arr:
    if i == maximum:
        continue
    print(i)