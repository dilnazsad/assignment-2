import statistics

a = input('enter your array:\n')
arr = list(map(int, a.split()))

mean = statistics.mean(arr)

for i in range(len(arr)):
    if arr[i] == 0:
        arr[i] = mean
print('Changed array:', arr)
