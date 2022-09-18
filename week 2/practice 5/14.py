text = input('enter your text:\n')
for word in text.split():
    if word.startswith("a") or word.endswith("i"):
        print(word)