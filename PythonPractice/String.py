# operations perform on string 

# reverse a string
a = "Hello World"
print(a)
print(a[::-1])

# to find length of string 
print(len(a))

# for dictionary of word
print(dir(a))

# to get specific part of string
print(a[0:5])

# we can also print by taking step in charcters
print(a[0:11:2])

# if string conataining alphabet and number
x =a.isalnum()
print(x)

# if only alphabet
print(a.isalpha())

# if only digits
print(a.isdigit())

# if in upper ase or lower case
print(a.isupper())
print(a.islower())

# to check first letter of world is captial or not
print(a.istitle()) 

# title used to make first letter of world is captial 
print(a.title())

# to replace an alphabet with another 
b = a.replace("o","OOO")
print(b)

# to remove space 
c = "       Hello I am python      " 
print(c)
print(c.strip()) 
print(c.lstrip()) # to remove space from left
print(c.rstrip())  # to remove space from right


# to remove any character
# srtip only remove charcter from start and ending
d = "-----Hello world------"
print(d.strip("-"))
print(d.lstrip("-")) # to remove space from left
print(d.rstrip("-"))  # to remove space from right

# to check with start with any sentence
e = "Hii I am python here!"
print(e.startswith("Hello")) # use for only single word

# if you want multiple word o check (use it in touple)
print(e.startswith(("Hello","Hii","Good morning")))

# similary endswith
print(e.endswith("here!"))


# case modification
x = "HeLLo WoRlD"
print(x.capitalize())  # only make first letter capital

# to make all letter small
print(x.casefold())
print(x.lower())

# swapcase for vice-versa
print(x.swapcase())

# captilization of all letter
print(x.upper())

# captilization only first sentence
print(x.title())


# to breake string like in list form
y = "hello world I am python here!"
print(y.split())

# you can also breake string where you want at specific
print(y.split("o"))

print(y.split("world")) 

# to split string with specific type
x = "A B C D E F G"
print(x.split(" ",2))
print(x.rsplit(" ",2))


# to join list into string
a = ["A","B","C","D"]
print(" ".join(a))
print("---".join(a))


# finding word
y = "hello world I am python here!"
print(y.find("o")) # gives index value of that letter
print(y.rfind("o"))

# for same we can use index
print(y.index("o"))
print(y.rindex("o"))

#concatination of string
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)

age = 20
text = "My age is "
print(text + str(age))


# format method in string
# {} are placeholder in pyhton it will replace our text with {} while executing

age = 20
text = "I am {} year old"  #I am -- year old
print(text.format(age))

# for multiple value
age = 20
school = "ABCD University"
text1 = "I am {} year old & I studied in {}"  #I am 20 year old I studied in ABCD University
print(text1.format(age,school))

# another method
text2 = "I am {} year old & I studied in {}".format(age,school)
print(text2)

# another method
text3 = f"I am {age} year old & I studied in {school}"
print(text3)