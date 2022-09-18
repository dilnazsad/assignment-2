s1 = input('enter the first array: ')
arr1 = list(map(int, s1.split()))
a2 = input('enter the second array: ')
arr2 = list(map(int, a2.split()))

arr2, arr1 = arr1, arr2
print('first array:', arr2)
print('second array:', arr1)
