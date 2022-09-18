i = 0
n = 0
text = input('enter your text:\n')
for i in range(len(text)):
    if text[i] == 'a':
        n += 1
print(text.replace('a', 'o'))
print(n)
print(len(text))

