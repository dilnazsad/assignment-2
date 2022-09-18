a = input("enter your array:\n")
arr = list(map(int, a.split()))

minimum = 10000
for i in range(len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]
        n = i

print('minimum element:', minimum)
print('index of the minimum element:', n)
