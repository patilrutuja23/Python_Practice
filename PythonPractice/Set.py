s = {12,34,3,67,5,76,35,98,6,767}
print(s)
# Unordered means that the items in a set do not have a defined order.
# Set items are unchangeable
# set does not repeat values/ duplicate not allowed.
s = {12,34,3,67,5,76,35,12,67,34,98,6,767}
print(s)

# True and 1 is considered the same value:
# False and 0 is considered the same value:

s1 = {"apple",21,32,1,True}
print(s1)

# For length of set
print(len(s))

# also make set using set() constructor
s2 = set((12,4,56,7,5,324,67))
print(s2)

# to add item
s1.add("hii")
print(s1)

# to mix two set
s1.update(s2)
print(s1)

# discard not raise error
s1.discard(80)
print(s1)

# remove raise error
s1.remove(7)
print(s1)

# as no index in set we can't predict what is going to pop
s1.pop()
print(s1)

a = {1,2,3,4,5,6,7}
b = {3,4,6,7,8,9,10}  

c = a.union(b) 
print(c)

d = a.intersection(b)
print(d)

e = a.symmetric_difference(b)
print(e)

f = a - b
print(f)

