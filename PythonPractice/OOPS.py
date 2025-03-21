
class Customar:
    # class attribute
    name = "ABCD"
    # methods(funciton)
    def greet():
        print("Hello welcome to bank")
    
c1 = Customar() # creating object for class
print(c1.name)  # calling by creating object 

# you can crate multiple object for a class
c2 = Customar
print(c2.name)
c2.greet()


class Customar:
    def __init__(self, name, age, amt):
        self.name = name
        self.age = age
        self.balance = amt
        
    def deposit(self, amount):
        self.balance += amount
        print(f"deposite of ₹{amount} is succcessful. Current balance is ₹{self.balance}") 
        
        
c3 = Customar("Rutuja",20,10000)
print(c3.name)
print(c3.age)
print(c3.balance)

c4 = Customar("Vidya",24,15000)
print(c4.name)
print(c4.age)
print(c4.balance)

c3.deposit(300)


# Method types

class School:
    school_name = "ABCD School"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name : {self.name} \nAge : {self.age}")
        
    # decorator for printing school name
    @classmethod
    def get_school(cls):
        return cls.school_name
    
    @staticmethod
    def is_adult(age):
        return age >= 18
    
x = School("Jonh",31)   
x.display()
print(x.get_school())
print(x.is_adult(19))


# Passsing Value
class Engine():
    def __init__(self):
        self.power = 100
    
    def start(self):
        print("Engine Start")
        
class Car:
    def __init__(self):
        self.engine = Engine()
        
    def move(self):
        self.engine.start()
        print("car is moving")
        
c = Car()
c.move()
        
    
# Inner class
class Outer():
    
    def __init__(self):
        self.x = 10
        
    class Inner():
        def __init__(self):
            self.y = 20
            # inside inner class
        def display():
            print("Inner Class")
            
    # inside outer class
    def display():
            print("Outer Class")
            
out = Outer()
in_class = out.Inner()



# Constructor in Incapsulation

# class Car:
#     __price = 5500 #this give error 'Car' object has no attribute 'price'

# c = Car()
# print(c.price)

# for that
class Car:
    __price = 5500
    
    def display_price(self):
        print(f"Price of car is {self.__price}")

c = Car()
c.display_price()


# Constructor in Inheritance

# Single level Inheritance
class A:
    def A(self):
        print("I am class A")
    
class B(A):
    def B(self):
        print("I am class B")
        
ob = B()
ob.A()
ob.B()

# Multiple level Inheritance
class A:
    def A(self):
        print("I am class A")
    
class B:
    def B(self):
        print("I am class B")
        
class C(A,B):
    def C(self):
        print("I am class C")
        
ob = C()
ob.A()
ob.B()
ob.C()


# Multilevel level Inheritance
class A:
    def A(self):
        print("I am class A")
    
class B(A):
    def B(self):
        print("I am class B")
        
class C(B):
    def C(self):
        print("I am class C")
        
ob = C()
ob.A()
ob.B()
ob.C()


# Heirarchical level Inheritance
class A:
    def A(self):
        print("I am class A")
    
class B(A):
    def B(self):
        print("I am class B")
        
class C(A):
    def C(self):
        print("I am class C")
        
ob = A()
ob1 = B()
ob.A()
ob1.B()
ob1.A()


# method Overriding
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Child(Parent):
    def __init__(self, name, age, school):
        Parent.__init__(self, name, age)
        self.school = school
    
ob = Child("John",20,"ABCD")
print(ob.name)
print(ob.age)
print(ob.school)

# super keyword
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)  # while using super keywoed do not use self keyword
        self.school = school
        
ob = Child("John",20,"ABCD")
print(ob.name)
print(ob.age)
print(ob.school)        
        
        
        
# Errors and Exceptions
# try...except...else...finally

try:
    print("hello")
    print(10/0)
except:
    print("Error Occurs, Something went wrong")
else:
    print("No error occur")    
finally:
    print("Block runs smoothly")
    
x = 2   
try:
    print(x)
    print(10/0)
except ZeroDivisionError:
    print("Error Occurs, divide by zero not possible")
except NameError:
    print("Error Occurs, divide by zero not possible")
    
# you can write your own exception
# class InvalidNumber(Exception):
#     pass
# x = int(input("Enter number between 0 to 10: "))
# if 0 <= x <= 10:
#     print("Correct Value")
# else:
#     raise InvalidNumber(f"{x} is not in range of 0 to 10")



# polymorphism : overloading and overriding

#method Overriding
def f1():
    print("one")

def f1():
    print("TWO")

def f1():
    print("THREE")
    
f1()


# overloading
def f1(x, y=None, z=None):
    if y and z:
        print(x*y*z)
    elif y:
        print(x+y)
    else:
        print(x)
f1(2,3,4)
    
    
# Duck Typing
def fun(a,b):
    return a+b

print(fun(2,4))
print(fun("hello ", "world"))



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)

ob = Rectangle(5,3)
print(ob.area())
print(ob.perimeter())
    
        
        
def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        
print(divide(10,0))

# file handeling

# f = open('Trial.py','x')
# f.close()

# either try this way

try:
    f = open('Trial.py','x')
    f.close()
except:
    print("File already exist with this name")


# rather writing close statement you can try
# with keyword

# write will override the data in file
with open('Trial.py','w') as f:
    f.write("Using with keyword I am writing in Trial.py file")


# append will enter data at last of the file
with open('Trial.py','a') as f:
    f.write("\nUsing with keyword I am appending in Trial.py file")
# we can also create new file with both a and w

with open('Trial.py') as f:
    print(f.read())
# read is default

with open('Trial.py','r') as f:
    f.seek(5) #to open file from that bit
    print(f.tell()) # tell starting bit
    print(f.read())
    print(f.tell())  # tell ending bit

 
 
# ""pickle ""
# pickling is storing file in binary file
# has method dump() for serialisation and load() for deserialisation
# we need to import pickle first

# here w't' or a't' or w'b' ab stand for file type example b=bin t=text

import pickle

# dump() [to make file into binary]
result = {'a':1, 'b':2, 'c':3}
with open('pickle.bin','wb') as f:  #bin for binary 
    pickle.dump(result,f)
    f.close
    
# load() [to return file into its real form]
with open('pickle.bin','rb') as f:  #bin for binary 
    x = pickle.load(f)

print(x)
print(type(x))


# zipping file
import zipfile

with zipfile.ZipFile('Python_course','w') as archive:
    archive.write('Trial.py')
    archive.write('pickle.bin')
    
# for unzipping all files
with zipfile.ZipFile('Python_course','w') as archive:
    archive.extractall()