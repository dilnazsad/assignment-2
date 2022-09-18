arr = [10, 14, 8, 32, 28, 45, 5, 2]

y = []

for i in arr:
    if i < 10:
        y.append(i)

x = arr.replace(y, 0)

print(x)