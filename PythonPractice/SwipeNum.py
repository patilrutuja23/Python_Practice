a = 5
b = 6

print(a)
print(b)

# method 1
a,b = b,a
print("After swapping")
print(a)
print(b)


# method 2
a = a+b
b = a-b
a = a-b
print("After swapping")
print(a)
print(b)


# method 3
a = a^b
b = a^b
a = a^b
print("After swapping")
print(a)
print(b)
