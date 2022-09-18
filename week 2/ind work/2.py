def change(list):
    size = len(list)

    temp = list[0]
    list[0] = list[size - 1]
    list[size - 1] = temp

    return list


a = input("enter your array:\n")

arr = a.split()

print("Swapped array", change(arr))