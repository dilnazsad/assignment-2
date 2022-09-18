def removeDuplicates(arr, n):

    res = list(range(10))

    j = 0
    for i in range(0, n - 1):

        if arr[i] != arr[i + 1]:
            res[j] = arr[i]
            j += 1

    res[j] = arr[n - 1]
    j += 1

    for i in range(0, j):
        arr[i] = res[i]

    return j


arr = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
n = len(arr)

n = removeDuplicates(arr, n)

for i in range(n):
    print(arr[i], end=" ")
