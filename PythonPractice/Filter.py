

ages = [1,23,18,45,60,3,12]
def adult(x):
    return x>=18

adults =  list(filter(adult,ages))
print(adults)

# also done as
ages = [1,23,18,45,60,3,12]

adults =  list(filter(lambda x: x>=18,ages))
print(adults)


num = (12,23,3,4,70,56,67,77,978)
def even(n):
    if n%2 == 0 :
        print(n," is a even number")
        
evenNum = tuple(filter(even,num))
print(evenNum)