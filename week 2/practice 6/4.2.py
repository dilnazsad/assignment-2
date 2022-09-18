arr = [10, 21, 7, 45, 66, 93]
i = 0

arr.sort()

print("Odd numbers:")

while i < len(arr):

    if arr[i] % 2 != 0:
        print(arr[i], end=" ")
    i += 1


