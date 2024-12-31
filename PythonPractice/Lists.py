# Lists in pyhton

list =[12,234,34,12,76,67]
str1 =['rutu', 'vidya','shruti']

print(type(list))
print(list)
print(str1)

mix = [list,str1]
print(mix)

# to add element at end
list.append(45)
print(list)

# to add element at position
list.insert(1,20)
print(list)

list.insert(2,29)
print(list)

# remove element from list
list.remove(234)
print(list)

# to remove using index
list.remove(list[3])
print(list)

list.pop(3)
print(list)

# to delete multiple elements from list
del list[2:]
print(list)

# to add multiple elements in list
list.extend([17,2,89,34,44])
print(list)

# to find minimum number
print(min(list))

# to find maximum number
print(max(list))

# to do sum of all number
s = sum(list)
print(s)

# to sort numbers
list.sort() 
print(list)

list.sort(reverse=True)
print(list)

print(list.__sizeof__)