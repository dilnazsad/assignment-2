def findDuplicates(arr, Len):

    duplicate = False

    result = []
    for i in range(Len - 1):
        for j in range(i + 1, Len):

            if arr[i] == arr[j]:
                if arr[i] in result:
                    break

                else:
                    result.append(arr[i])
                    duplicate = True

    if duplicate:
        print(result, end=" ")
    else:
        print("No duplicates present in arrays")


arr = [12, 11, 40, 12, 5, 6, 5, 12, 11]
n = len(arr)

findDuplicates(arr, n)

