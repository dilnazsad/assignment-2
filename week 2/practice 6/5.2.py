a = input("enter your array:\n")
arr = list(map(int, a.split()))

arr = list(dict.fromkeys(arr))
print(arr)
