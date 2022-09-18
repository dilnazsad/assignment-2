i = 0
n = 1
s = input('enter your text:\n')
for i in range(len(s)):
    if s[i] == ' ':
        n += 1
    if s[i] == '.':
        break
print(n)
