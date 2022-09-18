a = input("enter your array:\n")
arr = list(map(int, a.split()))

max_even = -2147483648
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        if arr[i] > max_even:
            max_even = arr[i]

print('Maximum even element:', max_even)
