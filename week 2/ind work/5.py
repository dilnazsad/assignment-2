def list_sort(lst):
    for i in range(len(lst)):
        lst[i] = abs(lst[i])

    return lst.sort(reverse=True)


arr = [34, 52, 8, 96, 56, 12, 82]


print('Numbers in descending order of their absolute value:', list_sort(arr))
