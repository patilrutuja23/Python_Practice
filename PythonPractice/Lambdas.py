# lambdas are small and anonymous function

def fun(x):
    return x+10

print(fun(5))
# instead of above function we can also do it as using lambda function

a = lambda x : x+10  # lambda always stored in variable
print(a(5))

a = lambda x,y,z : x+y+z
print(a(5,5,5))


# for avoiding similarities in code

def power(n):
    return lambda a : a ** n

square = power(2)
print(square(4))
cube = power(3)
print(cube(4))
fourth = power(4)
print(fourth(4))