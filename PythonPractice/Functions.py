
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
