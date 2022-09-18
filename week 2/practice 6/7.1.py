a = input("enter your array:\n")
arr = list(map(int, a.split()))

sum_even = 0
product_odd = 1
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        sum_even += arr[i]
    if arr[i] % 2 != 0:
        product_odd *= arr[i]

print('sum of even numbers:', sum_even)
print('product of odd numbers:', product_odd)
