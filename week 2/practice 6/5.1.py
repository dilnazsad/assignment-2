a = input("enter your array:\n")
arr = list(map(int, a.split()))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            if arr[i] < 0 and arr[j] < 0:
                print(arr[i], arr[j])
