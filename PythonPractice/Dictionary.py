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