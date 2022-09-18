a = input("enter your array:\n")
arr = list(map(int, a.split()))

pos = []
neg = []
for i in range(len(arr)):
    if arr[i] > 0:
        pos.append(arr[i])
    else:
        neg.append(arr[i])

print('positive elements:', pos)
print('other elements:', neg)
