a = input("enter your array:\n")
arr = list(map(int, a.split()))

oddnumbers = []
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        oddnumbers.append(arr[i])

for i in range(len(oddnumbers)):
    j = i + 1
    for j in range(len(oddnumbers)):
        if oddnumbers[i] < oddnumbers[j]:
            temp = oddnumbers[i]
            oddnumbers[i] = oddnumbers[j]
            oddnumbers[j] = temp

oddnumbers.reverse()
if not bool(oddnumbers):
    print('there are no odd elements')
else:
    print('sorted array with odd elements:', oddnumbers)
