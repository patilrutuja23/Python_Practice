# wrpper function or decorators functions  is function inside function

def mydecorator(func):
    def wrapper():
        print("Before function called")
        # now we are calling function
        func()
        print("After function called")
    
    return wrapper

# by using @mydecorator we can use wrapper function in simple way
@mydecorator
def hello():
    print("Hello Folk")
hello()



# without using @mydecorator we need to use this  
decorate = mydecorator(hello)
decorate()