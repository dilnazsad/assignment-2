s = input('enter your text:\n')
for word in s.split():
    if word.endswith("l"):
        print(word)
