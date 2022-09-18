i = 0
n = 0
s = input('enter your text:\n')
for i in range(len(s)):
    if s[i] == 'a':
        n += 1
print(s.replace('a', ''))
print(n)
