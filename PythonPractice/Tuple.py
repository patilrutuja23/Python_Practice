tup = (12,34,54,75,46,98,66)
print(tup)

print(tup[2])
# tuple are immutable


# to above attribute on tuple we need to conert tuple into list
l1 = list(tup)
# to add element at end
l1.append(45)
print(l1)

# to add element at position
l1.insert(1,20)
print(l1)

l1.insert(2,29)
print(l1)

# remove element from l1
l1.remove(46)
print(l1)

# to remove using index
l1.remove(l1[3])
print(l1)

l1.pop(3)
print(l1)

# after you can change it into tuple again
t1 = tuple(l1)
print(t1)


a=(1,2,3,2,3,4,5)
print(min(a)+max(a)+a.count(2))

T=tuple("tuple") 
print(T) 

#basic operation on tuple

# packing
t = ('A','B','C')
print(t)
a,b,c = t
print(a)
print(b)
print(c)

t = ('A','B','C','E','F','G','H')
print(t)
a,b, *c = t
print(a)
print(b)
print(c)

t = ('A','B','C','E','F','G','H')
print(t)
*a, b, c = t
print(a)
print(b)
print(c)

t1 = ('A','B','C','E')
t2 = ('E','F','G','H')
t3 = t1+t2
print(t3)
print(t1*3)

