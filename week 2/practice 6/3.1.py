import itertools

a = input("enter your array:\n")
arr = list(map(int, a.split()))

sum_odd = sum(itertools.islice(arr, 0, len(arr), 2))
print('entered array:\n', arr)
print('the sum of elements with odd indices:\n', sum_odd)
