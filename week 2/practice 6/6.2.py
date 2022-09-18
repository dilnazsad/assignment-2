lst = []
total = 0
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

    if numbers > 5:
        continue
    else:
        for ele in range(0, len(lst)):
            total = total + lst[ele]

print("The Sum of user input value is :", total)