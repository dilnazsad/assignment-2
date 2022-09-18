def EvenOddSum(a, n):
    even = 1
    odd = 1
    for i in range(n):

        if i % 2 == 0:
            even += a[i]
        else:
            odd *= a[i]

    print("Even index positions sum ", even)
    print("Odd index positions product ", odd)


arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)

EvenOddSum(arr, n)

