a = input("enter your array:\n")
arr = list(map(int, a.split()))

result = 0
for i in range(len(arr)):
    if arr[i] > 5:
        result += arr[i]

print('The sum of numbers that grater than 5:', result)
