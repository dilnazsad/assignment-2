a = input("enter your array:\n")
arr = list(map(int, a.split()))

maximum = 0
for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
        n = i

print('maximum element:', maximum)
print('index of the maximum element:', n)
