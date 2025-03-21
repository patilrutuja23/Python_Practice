# regular expression
# RegEx

import re
text = 'Hello World! I am Python and I am programming langauge.'
pattern = 'o'

# findall(what you want to find, from what)
x = re.findall(pattern, text)
print(x)

# search(what you want to find, from what)
x = re.search(pattern, text) # search for the pattern
print(x)
print(x.span())  # will give position of pattern

# give that group of pattern
print(x.group())


# split(what you want to split, from what)
x = re.split(pattern, text)
print(x)

x = re.split(pattern, text,2)
print(x)

# for subtitute
x = re.sub(pattern, "***", text)
print(x)




sentence='we are humans'
matched=re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())





text = 'Hello World! I am Python and I am programming langauge.'
pattern = 'H....o'
x = re.findall(pattern, text)
print(x)

text = 'Hello World! I am Python and I am programming langauge.'
pattern = 'H...o'
x = re.findall(pattern, text)
print(x)

text = 'Hello World! I am Python and I am programming langauge.'
pattern = '.a.'
x = re.findall(pattern, text)
print(x)

text = 'Hello World! I am Python and I am programming langauge.'
pattern = '^Hello'  #^ is statement start with
x = re.findall(pattern, text)
print(x)

text = 'Hello World! I am Python and I am programming langauge.'
pattern = 'langauge$'  # $ is statement ends with
x = re.findall(pattern, text)
print(x)



# avoiding .... many times

# * : Any number of type including zero 
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not, this will give entire statement
pattern = 'a.*$'  
x = re.findall(pattern, text)
print(x)

# + : Any number of type excluding zero 
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = 'I.+$'  
x = re.findall(pattern, text)
print(x)

# ? : Exactly 0 or 1 time
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = 'I.?$'  
x = re.findall(pattern, text)
print(x)


# {} : for exact number of time
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = 'Hel{2}o'  
x = re.findall(pattern, text)
print(x)



# \A
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = '\AHello'  
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")


# \b check any specific match at the begining or at the end
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = r'\bWo'  # \b if put at backside of search use for end
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")

# \d for digits
text = 'Hello World! I am Python and I am programming langauge 23.'
# check for is string have that charcter or not
pattern = '\d'  
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")


# \D other than digits
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = '\D'  
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")


# \s for spaces in string
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = '\s'  
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")


# \S for other than spaces in string
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = '\S'  
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")



# \w for legal charcter in python
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = '\w'  
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")
    
    
# \W for illegal charcter in python
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = '\W'  
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")
    

# \Z for to check at end of the string in python
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = r'.\Z'  
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")
    
    

# [] for to check range of character in the string in python
text = 'Hello World! I am Python and I am programming langauge.'
# check for is string have that charcter or not
pattern = '[a-s]'  #for charcter present
pattern = '[^b-f]'  # ^ used for except
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")
    
    
# [][] for to check range of character in the string in python
text = 'Hello World! I am Python and I am programming langauge 23.'
# check for is string have that charcter or not
pattern = '[0-5][1-9]'  # [tens place] [unit place]
x = re.findall(pattern, text)
print(x)
if x:
    print("There is a match")
else:
    print("No match found")
