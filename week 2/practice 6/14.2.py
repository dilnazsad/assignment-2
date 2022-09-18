import statistics


a = input("enter your array:\n")
arr = list(map(int, a.split()))

mean = statistics.mean(arr)

for i in range(len(arr)):
    if arr[i] > mean:
        arr[i] = 1
print('changed array:', arr)
