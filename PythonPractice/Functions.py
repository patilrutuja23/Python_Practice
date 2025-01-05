
# defining function
def greeting():
    print("hello world")
    
# calling functions
greeting()


# also use  return type
def greeting():
    return "hello world"
    
print(greeting())


# we can also use function like
def num():
    a=1
    b=2
    return a,b

n1,n2 = num()
print(n1)
print(n2)

# this can also write as
def num():
    a=1
    b=2
    return (a,b)

result = num()
print(result)


# use function as arguments
# this multiply function is called as argument in apply function
def multiply(x,y):
    return x*y

# here func argument is used to call multiply function while calling apply function 
def apply(func, x,y):
    return func(x,y)

result = apply(multiply,5,2)
print(result)


# formal argument
def fun(x,y):
    return x*y
 # here fun(x,y)=fun(5,2)
print(fun(5,2))


# Actual argument / pass by reference
def myfun(myList):
    myList.append(1)
    
l1 = [2,3,4]
print(l1)
myfun(l1)
print(l1)


# arbitory argument
# * use to make it touple
def myfun(*name):
    for name in name:
        print("hello",name)
    
myfun("rutuja","mohini","shruti")


# Arbitory keyword argument
# ** too use as dictionary
def myfun(**detail):
    print(detail)

myfun(Name="Rutuja",Surname="Patil",Age=20)