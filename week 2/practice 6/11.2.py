a = input("enter your array:\n")
arr = list(map(int, a.split()))

arr2 = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        if arr[i] < 10:
            arr2.append(arr[i])
if not bool(arr2):
    print('there are no even numbers of the original array less than 10')
else:
    print('even numbers of the original array less than 10:', arr2)
