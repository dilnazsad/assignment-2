s = input('enter your text:\n')
left = s.find('(')
right = s.find(')')
print(s[left + 1:right])
