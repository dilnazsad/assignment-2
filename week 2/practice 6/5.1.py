def printPairs(arr, n):
    hs = set()
    for i in range(n):
        if (arr[i] * -1) in hs:

            if arr[i] < 0:
                print(arr[i], end=" ")
                print((arr[i] * -1), end=" ")

            else:
                print((arr[i] * -1), end=" ")
                print(arr[i], end=" ")

        hs.add(arr[i])
    return


arr = [4, 8, 9, -4, 1, -1, -8, -9]
n = len(arr)
printPairs(arr, n)