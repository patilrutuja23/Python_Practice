# Generators has entity "yield" 

def gener():
    yield 1 # this are keyword
    yield 2
    yield 3
    
for x in gener():
    print(x)
    print(x,"is a number")
    
# or we can also do 
x = gener()
print(next(x))
print(next(x))
print(next(x))


# for example we can do fibbonacci series
def fibo(limit):
    a,b = 0,1
    while a <= limit :
        yield a
        a,b = b, a+b
    
for num in fibo(100):
    print(num,end=" ")


# you can either use this method to run
x = fibo(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

