dic = {1:'rutuja',2:'aditya',4:'vidya'}
print(dic)

# to get keys and values from dict
print(dic.keys())
print(dic.values())



# to access data from dictionary, key in [] are data key like 1,2,4
print(dic[2])

# for accessing data value using index
print(dic.get(1))

# if we don't have element present at that specific key we can print any statement at that place
print(dic.get(6, 'Not found'))

# we can also create dictinory like:

key = ['Navin','Rutuja','Mohini','Vidya']
value = [39,19,20,24]
d = dict(zip(key,value))
print(d)

# to add element in dictionary
dic[3] = 'Mohini'
print(dic)

# to delete from dictionary
del dic[4]
print(dic)

# new type of dictionary
prog = {'js':'atom', 'cs':'vs','python':('pycharm','sublime'),'java':{'jse':'netbean','jee':'eclipse'}}
print(prog)

print(prog['js'])
print(prog['python'])
print(prog['java'])
print(prog['python'][1])
print(prog['python'][0])

print(prog['java']['jee'])

print(prog.items())

# making dic using list

d1 = [('a',1),('b',2),('c',3),('d',4)]
d2 = dict(d1)
print(d1)
print(type(d1))
print(d2)
print(type(d2))



# to print string into dict
import ast

s = "{1:'rutuja',2:'aditya',4:'vidya'}"
d = ast.literal_eval(s)
print(d)

# to change value
d1 = {'Navin': 39, 'Rutuja': 19, 'Mohini': 20, 'Vidya': 24}
d1['Rutuja'] = 20
print(d1)

# also use update method
d1.update({'Vidya': 25})
print(d1)

d1.update({'Aditya': 17})
print(d1)

# remove item
d1.pop('Navin')
print(d1)

d1.popitem()
print(d1)

# delete item
del d1['Mohini']
print(d1)


count={}
count[(1,2,4)] =5
count[(4,2,1)] =7
count[(1,2)]= 6
count[(4,2,1)] =2
tot= 0
for i in count:
    tot=tot+count[i]
print(len(count)+tot)



a={i: i*i for i in range(6)}
print(a)



# looping in dictionary
d1 = {'Navin': 39, 'Rutuja': 19, 'Mohini': 20, 'Vidya': 24}
# to get Keys
for x in d1.keys():
    print(x)
# to get values
for x in d1.values():
    print(x)
# to get both key and values
for x in d1.items():
    print(x)
        
for key, value in d1.items():
    print(f"The key is {key= } and the pair value is {value= }")
    
    
    
    
# sorting
d = {'c': 3, 'b': 2, 'd': 4, 'a': 1}
print(dict(sorted(d.items())))

# sorting with value
d = {'c': 8, 'b': 5, 'd': 3, 'a': 1}
s = dict(sorted(d.items(), key=lambda item: item[1]))
print(s)

# conacatinate or merge two dict
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = d1.update(d2)
print(d3)

d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}
d1.update(d2)
print(d1)

# Using Dictionary Unpacking (**)
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}
d3 = {**d1, **d2}
print(d3)

# Using | Operator 
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}
d3 = d1 | d2
print(d3)


