a = input("enter your array:\n")
arr = list(map(int, a.split()))

sum = 1
for i in arr:
    sum = sum + i

print("sum of elements:", sum)

product = 1
for i in arr:
    product = product * i

print("product of elements:", product)
