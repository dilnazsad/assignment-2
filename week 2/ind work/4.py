def useless(a):
    maximum = 0
    for i in range(len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum / len(a)


arr = [34, 52, 8, 96, 56, 12, 82]

print('Useless number:', useless(arr))