array = [[1, 2, -3, -4], [-2, 3, -1, 5]]

array.sort(key=lambda x: sum(map(lambda xy: abs(xy), x)), reverse=True)

print(array)