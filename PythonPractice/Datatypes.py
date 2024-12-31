a = 1
b = -4
c = 10.3
d = -9.8
e = 2e3
f = 12+5j

h="rutuja patil"

print(a) 
print(b)
print(c) 
print(d) 
print(e)
print(f)  

# operations on string
print('r'*5)
print('5*r')

print(h)
print(h[1])
print(h[0:6])


# to find address of an data
print(id(a))

# if data is same then address is also same
x = 10
y = 10
print(id(x)) 
print(id(y)) 
print(id(10)) 
if x==y:
    print('hii')
    
# we can also write complex number like
c1 = 3
c2 = 5
c3 = complex(c1,c2)
print(c3)