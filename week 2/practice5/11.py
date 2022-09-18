import re
text = input('enter your text:\n')
n = re.findall('[Nn]+', text)
n_len = map(len,n)
print(max(n_len))
print(text.replace('!', '.'))