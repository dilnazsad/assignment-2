a = input("enter your array:\n")
arr = list(map(int, a.split()))

min_odd = 10000
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        if arr[i] < min_odd:
            min_odd = arr[i]

print('minimum odd element:', min_odd)
