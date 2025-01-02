import re

text = "My phone number : 9090909090"
pattern = r"\d\d\d\d\d\d\d\d\d\d"
match = re.search(pattern,text)
if match:
    print("phone number: ",match.group())
else:
    print("not found")
    