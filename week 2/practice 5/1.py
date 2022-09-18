import re

text = input("enter your text in russian:\n")

list = re.findall("е", text)

print(len(list))